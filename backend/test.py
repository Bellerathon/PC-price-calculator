from bs4 import BeautifulSoup
import requests
import numpy as np
from re import sub
from decimal import Decimal

def reject_outliers(data):
    m = 2
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    return round(sum(data[s<m]) / len(data[s<m]))

nonti_gpu_filters = "+-cooling+-fan%2C+-fan%2C+-laptop%2C+-broken%2C+-shroud%2C+-hdd%2C+-motherboard%2C+-ram%2C+-cpu"
ti_gpu_filters = "+-cooling+-fan%2C+-fan%2C+-ti%2C+-laptop%2C+-broken%2C+-shroud%2C+-hdd%2C+-motherboard%2C+-ram%2C+-cpu"
motherboard_filters = 


ebayUrl = "https://www.ebay.com.au/sch/i.html?_udlo=60&_fosrp=1&_osacat=0&_mPrRngCbx=1&LH_ItemCondition=4&_ipg=60&LH_Complete=1&_odkw=asus+strix+gtx1070+-cooling+-fan%2C+-fan%2C+-ti%2C+-laptop%2C+-broken%2C+-shroud%2C+-hdd%2C+-motherboard&LH_Sold=1&_dmd=1&_stpos=2000&_sop=13&_sadis=15&_from=R40&_trksid=p2045573.m570.l1313&_nkw=asus+strix+gtx1070&_sacat=0"

request = requests.get(ebayUrl)
soup = BeautifulSoup(request.text, "html.parser")

listings = soup.find_all("span", class_ = "bold bidsold")
# prices = [460.00,   386.00,   370.00,   450.00,   500.00,   331.00,   414.42, 426.41, 373.11, 474.32,
#  439.74, 426.41, 491.91, 413.09, 360.15, 395.28, 466.39, 456.77, 549.67, 527.04,
#  356.63]
prices = []
for listing in listings:
    # price = listing.text
    # price = price.split("$")[1]
    price = price.strip()
    value = Decimal(sub(r'[^\d.]', '', price))
    print(value)
    prices.append(value)

numpy_prices = np.array(prices).astype(np.float)
filtered_prices = reject_outliers(numpy_prices)
print(filtered_prices)
