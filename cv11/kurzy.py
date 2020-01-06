import requests
import sys

URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/\
kurzy-devizoveho-trhu/denni_kurz.txt"

thecode = sys.argv[1]

res = requests.get(URL)
print(res)
lines = res.text.split("\n")[2:-1]
for l in lines:
    (country,currency,amount,code,rate) = l.split("|")
    #print(code,rate)
    if code == thecode:
        print("{} {}:{}".format(country,amount,rate))

# v sys.argv[1] je kod meny
# vypise nazev statu a kurz ve formatu mnozstvi:kurz



#03.01.2020 #2
#země|měna|množství|kód|kurz
#Austrálie|dolar|1|AUD|15,821
#Brazílie|real|1|BRL|5,599
#Bulharsko|lev|1|BGN|12,968
#Čína|žen-min-pi|1|CNY|3,264
#Dánsko|koruna|1|DKK|3,393
#EMU|euro|1|EUR|25,360
#Filipíny|peso|100|PHP|44,508
#Hongkong|dolar|1|HKD|2,925
#Chorvatsko|kuna|1|HRK|3,406