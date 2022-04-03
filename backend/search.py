from difflib import SequenceMatcher
import json
from threading import local
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from bs4 import BeautifulSoup
import requests
import numpy as np
from re import sub
from decimal import Decimal
from datetime import datetime
from collections import namedtuple
from operator    import itemgetter

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
valid_parts = ["CPU", "GPU", "MOTHERBOARD", "RAM", "STORAGE", "FAN", "CASE", "POWERSUPPLY", "KEYBOARD", "MOUSE", "MONITOR", "COOLER"]

@app.route('/searchPart', methods=['POST'])
@cross_origin()
def searchPart():
    data = request.get_json(force=True)
    part = secure_filename(data["part"])
    target = data["name"]
    print(target)
    if part not in valid_parts:
        return jsonify("Invalid part")
    f = open(f"/home/will/pcprice/backend/parts/{part}.txt", "r")
    similar_array = []
    for line in f:
        cpu = {}
        line = line.strip("\n")
        if SequenceMatcher(None, target, line).ratio() == 1.0:
            return jsonify(line)
        else:
            cpu["name"] = line
            current_similarity = SequenceMatcher(None, target, line).ratio()
            cpu["similarity"] = current_similarity
            similar_array.append(cpu)

    f.close()

    newlist = sorted(similar_array, key=lambda d: d["similarity"])
    newlist = reversed(newlist)
    cpus = []
    for index, cpu in enumerate(newlist):
        if index == 15:
            break
        cpus.append(cpu["name"])
    print(cpus)
    return jsonify(cpus)

@app.route('/searchPartPrice', methods=['POST'])
@cross_origin()
def searchPartPrice():
    data = request.get_json(force=True)
    id = data["part"]
    part = data["name"]
    print(part, id)
    BASE = "https://www.ebay.com.au/sch/i.html?_from=R40&_fosrp=1&_nkw="
    GPU2 = "&_ex_kw=cpu+motherboard+ram+tower+pc+cooling+fan+shroud+fan+broken+laptop+faulty+read"
    GPU3 = "&_ex_kw=cpu+motherboard+ram+tower+pc+cooling+fan+shroud+fan+broken+laptop+faulty+read+ti+Ti+TI"
    CPU ="https://www.ebay.com.au/sch/i.html?_from=R40&_fosrp=1&_nkw=%22Intel%22+%22Core%22+%22i7-6700k%22&_in_kw=1&_ex_kw=gpu+motherboard+ram+computer+pc+tower&_sacat=0&LH_Sold=1&_udlo=&_udhi=&_samilow=&_samihi=&_sadis=15&_stpos=2000&_sargn=-1%26saslc%3D1&_salic=15&_sop=13&_dmd=1&_ipg=60&LH_Complete=1"
    MOTHERBOARD = "https://www.ebay.com.au/sch/i.html?_from=R40&_fosrp=1&_nkw=%22ASRock%22+%22B550%22+%22Steel%22+%22Legend%22+%22AM4%22+%22ATX%22&_in_kw=1&_ex_kw=gpu+cpu+ram+tower+pc&_sacat=0&LH_Sold=1&_udlo=&_udhi=&_samilow=&_samihi=&_sadis=15&_stpos=2000&_sargn=-1%26saslc%3D1&_salic=15&_sop=13&_dmd=1&_ipg=60&LH_Complete=1"
    RAM = "https://www.ebay.com.au/sch/i.html?_from=R40&_fosrp=1&_nkw=PART&_in_kw=1&_ex_kw=cpu+gpu+motherboard+tower+2x+3x+4x+lot+x2+x3+x4&_sacat=0&LH_Sold=1&_udlo=&_udhi=&_samilow=&_samihi=&_sadis=15&_stpos=2000&_sargn=-1%26saslc%3D1&_salic=15&_sop=13&_dmd=1&_ipg=60&LH_Complete=1"
    END = "&_in_kw=1&&_sacat=0&LH_Sold=1&_udlo=&_udhi=&LH_ItemCondition=4&_samilow=&_samihi=&_sadis=15&_stpos=2000&_sargn=-1%26saslc%3D1&_salic=15&_sop=13&_dmd=1&_ipg=60&LH_Complete=1"
    
    searchString = ""
    if id == "GPU":
        searchString = BASE
        for part in part.split(" "):
            part = "\"" + part + "\"" + "+"
            searchString += part
        searchString = searchString[:-1]
        if "Ti" not in part:
            searchString += GPU3
        else:
            searchString += GPU2
        searchString += END
    else:
        searchString = BASE
        for part in part.split(" "):
            part = "\"" + part + "\"" + "+"
            searchString += part
        searchString = searchString[:-1]
        searchString += END
    
    print(searchString)

    req = requests.get(searchString)
    soup = BeautifulSoup(req.text, "html.parser")

    listings = soup.find("ul", {"id": "ListViewInner"})
    children = listings.findChildren("li", recursive=False)

    prices = []
    for child in children:
        price = child.find("span", class_ = "bold bidsold")
        if price == None:
            prices.append("International sellers")
            continue
        price = price.text
        price = price.split("$")[1]
        price = price.strip()
        value = (sub(r'[^\d.]', '', price))
        prices.append(float(value))

    index_split = prices.index("International sellers")
    local_sellers = prices[:index_split]
    international_sellers = prices[index_split + 1:]

    if len(local_sellers) == 0:
        return jsonify(international_sellers)

    return jsonify(local_sellers)

# Credit: u/Benjamin Bannier - https://stackoverflow.com/questions/11686720/is-there-a-numpy-builtin-to-reject-outliers-from-a-list
def reject_outliers(price_array):
    numpy_prices = np.array(price_array).astype(np.float)
    m = 7.
    d = np.abs(numpy_prices - np.median(numpy_prices))
    mdev = np.median(d)
    s = d/mdev if mdev else 1.
    prices = numpy_prices[s<m]
    print(prices)
    return prices.tolist()

# Credit: u/Daniel Reina - https://stackoverflow.com/questions/40057020/calculating-exponential-moving-average-ema-using-javascript
def EMA(price_array):
    k = 2 / (len(price_array) + 1)
    emaArray = [price_array[0]]
    for i in range(1, len(price_array), 1):
        emaArray.append(price_array[i] * k + emaArray[i - 1] * (1 - k))
    print(emaArray)
    return emaArray