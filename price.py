from urllib.request import Request, urlopen
import datetime
import time

req = Request('https://www.google.com/search?&q=bitcoin', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = webpage.decode("utf-8")

#price = urllib.request.urlopen("https://www.google.com/search?&q=bitcoin")
#html_bytes = price.read()
pricefind = html.find("United States Dollar")
currentprice = html[pricefind-10:pricefind-1]
currentprice = float(currentprice.replace(',',''))
buyin = None
buyinprice = None
currenttime = datetime.datetime.now()
currentunixtime = time.time()

print ("Today is " + str(currenttime.date()) + ".\nThe time is " + str(currenttime.time()) + "\n")

while buyin == None:
    buyin = float(input("How much did bitcoin you buy: "))
while buyinprice == None:
    buyinprice = float(input("How much was one bitcoin worth at the time: "))
    
moneyin = buyin * buyinprice
difference = ((currentprice/buyinprice) - 1)
print ("The current price for bitcoin is $" + str(currentprice) + ".")
if difference > 0:
    print ("Today it has increased by " + str(difference*100) + "%.")
else:
    print ("Today it has decreased by " + str(1-difference*100) + "%.")

End = input("Selling all of your bitcoin now will net you a profit of " + (str((buyin * currentprice)-moneyin)) + " dollars.")
