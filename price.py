#Doesn't work as coindesk has changed their website.
import urllib.request
price = urllib.request.urlopen("https://www.coindesk.com/price/bitcoin")

html_bytes = price.read()
html = html_bytes.decode("utf-8")
pricefind = html.find("class='typography__StyledTypography-owin6q-0 jvRAOp'")
currentprice = html[pricefind+49:pricefind+58]
print (currentprice)
currentprice = float(currentprice.replace(',',''))
buyin = None
buyinprice = None

while buyin == None:
    buyin = int(input("How much did bitcoin you buy? "))
while buyinprice == None:
    buyinprice = int(input("How much was it worth? "))
    
difference = ((currentprice/buyinprice) - 1)
print ("The current price is " + str(currentprice) + ".")
if difference > 0:
    print ("Today it has increased by " + str(difference*100) + "%.")
else:
    print ("Today it has decreased by " + str(1 - difference*100) + "%.")

print ("Your buy-in is currently at " + str((buyin + (buyin*(difference)))) + ".")

