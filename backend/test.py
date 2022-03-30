from bs4 import BeautifulSoup
import requests
import numpy as np
from re import sub
from decimal import Decimal
from datetime import date, datetime

def reject_outliers(data):
    m = 2
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    return round(sum(data[s<m]) / len(data[s<m]))

def findPrices():
    nonti_gpu_filters = "+-cooling+-fan%2C+-fan%2C+-laptop%2C+-broken%2C+-shroud%2C+-hdd%2C+-motherboard%2C+-ram%2C+-cpu"
    ti_gpu_filters = "+-cooling+-fan%2C+-fan%2C+-ti%2C+-laptop%2C+-broken%2C+-shroud%2C+-hdd%2C+-motherboard%2C+-ram%2C+-cpu"
    ram = "https://www.ebay.com.au/sch/i.html?_blrs=spell_check&_from=R40&_fosrp=1&_sacat=0&LH_Sold=1&_mPrRngCbx=1&_udlo&_udhi&LH_ItemCondition=4&_samilow&_samihi&_sadis=15&_stpos=2000&_sop=13&_dmd=1&_ipg=60&LH_Complete=1&_nkw=%22kingston%22%20%22fury%22%20%228%22%20%22gb%22%20%22ddr4%22%20%222400%22%20%22mhz%22&LH_LocatedIn=15&_dcat=170083&rt=nc"
    
    gpu = "https://www.ebay.com.au/sch/i.html?_udlo=60&_fosrp=1&_osacat=0&_mPrRngCbx=1&_ipg=60&LH_Complete=1&_odkw=%22asus%22+%22strix%22+%22gtx1070%22+-cooling+-fan%2C+-fan%2C+-laptop%2C+-broken%2C+-shroud%2C+-hdd%2C+-motherboard%2C+-ram%2C+-cpu%2C+-ti%2C+-hz%2C+-not+working&LH_Sold=1&_dmd=1&LH_LocatedIn=15&_stpos=2000&_sop=12&_sadis=15&_from=R40&_trksid=p2045573.m570.l1313&_nkw=%22asus%22+%22strix%22+%22gtx1070%22+-cooling+-fan%2C+-fan%2C+-laptop%2C+-broken%2C+-shroud%2C+-hdd%2C+-motherboard%2C+-ram%2C+-cpu%2C+-ti%2C+-hz&_sacat=0"
    cpu ="https://www.ebay.com.au/sch/i.html?_from=R40&_fosrp=1&_nkw=%22Intel%22+%22Core%22+%22i7-6700k%22&_in_kw=1&_ex_kw=gpu+motherboard+ram+computer+pc+tower&_sacat=0&LH_Sold=1&_udlo=&_udhi=&_samilow=&_samihi=&_sadis=15&_stpos=2000&_sargn=-1%26saslc%3D1&_salic=15&_sop=13&_dmd=1&_ipg=60&LH_Complete=1"
    motherboard = "https://www.ebay.com.au/sch/i.html?_from=R40&_fosrp=1&_nkw=%22ASRock%22+%22B550%22+%22Steel%22+%22Legend%22+%22AM4%22+%22ATX%22&_in_kw=1&_ex_kw=gpu+cpu+ram+tower+pc&_sacat=0&LH_Sold=1&_udlo=&_udhi=&_samilow=&_samihi=&_sadis=15&_stpos=2000&_sargn=-1%26saslc%3D1&_salic=15&_sop=13&_dmd=1&_ipg=60&LH_Complete=1"
    ram = "https://www.ebay.com.au/sch/i.html?_from=R40&_fosrp=1&_nkw=%22%22Crucial%22%22+%22%22Ballistix%22%22+%22%228GB%22%22+%22%22DDR4%22%22+%22%222400MHz%22%22&_in_kw=1&_ex_kw=cpu+gpu+motherboard+tower+2x+3x+4x+lot+x2+x3+x4&_sacat=0&LH_Sold=1&_udlo=&_udhi=&_samilow=&_samihi=&_sadis=15&_stpos=2000&_sargn=-1%26saslc%3D1&_salic=15&_sop=13&_dmd=1&_ipg=60&LH_Complete=1"


    location_australia = "&LH_PrefLoc=1"
    location_wordliwde = "&LH_PrefLoc=2"
    used = "&_dcat=27386&rt=nc&LH_ItemCondition=3000"
    sold = "&LH_Complete=1&LH_Sold=1&"
    
    request = requests.get(gpu)
    soup = BeautifulSoup(request.text, "html.parser")

    listings = soup.find("ul", {"id": "ListViewInner"})
    children = listings.findChildren("li", recursive=False)
    
    prices = []
    for child in children:
        # print(child)
        price = child.find("span", class_ = "bold bidsold")
        if price == None:
            # prices.append("International sellers")
            continue
        price = price.text
        price = price.split("$")[1]
        price = price.strip()
        value = sub(r'[^\d.]', '', price)
        prices.append(float(value))

    dates = []
    post_dates = soup.findAll("span", class_ = "tme")
    for d in post_dates:
        this_year = str(datetime.now().year)
        datestr = str(this_year) + "-" + d.text.strip()
        dates.append(datetime.strptime(datestr, '%Y-%d-%b %H:%M'))
    sorted_dates = sorted(dates)
    
    date_weights = []
    for post_date in sorted_dates:
        today = datetime.today().strftime('%Y-%d-%b %H:%M')
        today = datetime.strptime(today, '%Y-%d-%b %H:%M' )
        weight = today - post_date
        date_weights.append(float(weight.days))
    
    weighted_dates = [x / 10 for x in date_weights[::-1]]
    
    print(prices)
    avg = np.average(prices)
    print(avg)
    weighted_avg = np.average(prices, weights=weighted_dates)
    print(weighted_avg)

    index_split = prices.index("International sellers")
    local_sellers = prices[:index_split]
    international_sellers = prices[index_split:]

    if (len(local_sellers) > 0):
        numpy_prices = np.array(local_sellers).astype(np.float)
        return reject_outliers(numpy_prices)
    elif (len(local_sellers) == 0):
        numpy_prices = np.array(international_sellers).astype(np.float)
        return reject_outliers(numpy_prices)
    else:
        return unsold_listings()

def unsold_listings():
    return "hello"

# listings = soup.find_all("span", class_ = "bold bidsold")
# print(listings)
# # prices = [460.00,   386.00,   370.00,   450.00,   500.00,   331.00,   414.42, 426.41, 373.11, 474.32,
# #  439.74, 426.41, 491.91, 413.09, 360.15, 395.28, 466.39, 456.77, 549.67, 527.04,
# #  356.63]
# prices = []
# for listing in listings:
#     price = listing.text
#     price = price.split("$")[1]
#     price = price.strip()
#     value = Decimal(sub(r'[^\d.]', '', price))
#     print(value)
#     prices.append(value)

# numpy_prices = np.array(prices).astype(np.float)
# filtered_prices = reject_outliers(numpy_prices)
# print(filtered_prices)

if __name__ == "__main__":
    findPrices()