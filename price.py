from urllib.request import Request, urlopen

req = Request('https://www.google.com/search?&q=bitcoin', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = webpage.decode("utf-8")

#price = urllib.request.urlopen("https://www.google.com/search?&q=bitcoin")
#html_bytes = price.read()
pricefind = html.find("United States Dollar")
print (pricefind)
currentprice = html[pricefind-10:pricefind-1]
print (currentprice)
currentprice = float(currentprice.replace(',',''))
buyin = None
buyinprice = None

while buyin == None:
    buyin = float(input("How much did bitcoin you buy? "))
while buyinprice == None:
    buyinprice = float(input("How much was it worth? "))
    
difference = ((currentprice/buyinprice) - 1)
print ("The current price is " + str(currentprice) + ".")
if difference > 0:
    print ("Today it has increased by " + str(difference*100) + "%.")
else:
    print ("Today it has decreased by " + str(1 - difference*100) + "%.")

print ("Your buy-in is currently at " + str((buyin + (buyin*(difference)))) + ".")

