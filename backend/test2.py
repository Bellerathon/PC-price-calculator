part = "Intel Core i7-6700k"
id = "GPU"

GPU1 = "https://www.ebay.com.au/sch/i.html?_udlo=60&_fosrp=1&_osacat=0&_mPrRngCbx=1&_ipg=60&LH_Complete=1&_odkw="
GPU2 = "-cooling+-fan%2C+-fan%2C+-laptop%2C+-broken%2C+-shroud%2C+-hdd%2C+-motherboard%2C+-ram%2C+-cpu%2C+-ti%2C+-hz%2C+-not+working&LH_Sold=1&_dmd=1&LH_LocatedIn=15&_stpos=2000&_sop=12&_sadis=15&_from=R40&_trksid=p2045573.m570.l1313&_nkw=%22asus%22+%22strix%22+%22gtx1070%22+-cooling+-fan%2C+-fan%2C+-laptop%2C+-broken%2C+-shroud%2C+-hdd%2C+-motherboard%2C+-ram%2C+-cpu%2C+-ti%2C+-hz&_sacat=0"
CPU ="https://www.ebay.com.au/sch/i.html?_from=R40&_fosrp=1&_nkw=%22Intel%22+%22Core%22+%22i7-6700k%22&_in_kw=1&_ex_kw=gpu+motherboard+ram+computer+pc+tower&_sacat=0&LH_Sold=1&_udlo=&_udhi=&_samilow=&_samihi=&_sadis=15&_stpos=2000&_sargn=-1%26saslc%3D1&_salic=15&_sop=13&_dmd=1&_ipg=60&LH_Complete=1"
MOTHERBOARD = "https://www.ebay.com.au/sch/i.html?_from=R40&_fosrp=1&_nkw=%22ASRock%22+%22B550%22+%22Steel%22+%22Legend%22+%22AM4%22+%22ATX%22&_in_kw=1&_ex_kw=gpu+cpu+ram+tower+pc&_sacat=0&LH_Sold=1&_udlo=&_udhi=&_samilow=&_samihi=&_sadis=15&_stpos=2000&_sargn=-1%26saslc%3D1&_salic=15&_sop=13&_dmd=1&_ipg=60&LH_Complete=1"
RAM = "https://www.ebay.com.au/sch/i.html?_from=R40&_fosrp=1&_nkw=PART&_in_kw=1&_ex_kw=cpu+gpu+motherboard+tower+2x+3x+4x+lot+x2+x3+x4&_sacat=0&LH_Sold=1&_udlo=&_udhi=&_samilow=&_samihi=&_sadis=15&_stpos=2000&_sargn=-1%26saslc%3D1&_salic=15&_sop=13&_dmd=1&_ipg=60&LH_Complete=1"

if id == "GPU":
    searchString = GPU1
    for part in part.split(" "):
        part = "%22" + part + "%22+"
        searchString += part
    searchString += GPU2

print(searchString)