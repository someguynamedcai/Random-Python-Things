from urllib.request import Request, urlopen
import datetime
import time

req = Request('https://www.google.com/search?&q=euro+rate', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
html = webpage.decode("utf-8")

#price = urllib.request.urlopen("https://www.google.com/search?&q=bitcoin")
#html_bytes = price.read()
pricefind = html.find("United States Dollar")
currentprice = html[pricefind-5:pricefind-1]

print ("The current conversion of Euros to USD is " + currentprice + ".")
while (True):
    text = input("How much would you like to convert:")
    if text.isdigit():
        print ("That is " + str(float(currentprice)*float(text)) + " Euros.")
else:
    print("Invalid input. Please enter a number.")
