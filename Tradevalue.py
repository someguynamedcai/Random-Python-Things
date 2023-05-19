from urllib.request import Request, urlopen

while(True):
    url = "https://www.gamestop.com/trade/?q="
    game = input("Type in a game to search for: ")
    game = game.replace(" ", "+")

    url = url + game
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    html = webpage.decode("utf-8")
    pricefind = html.find("Up to:")
    price = html[pricefind+15:pricefind+20]
    print (game + " is worth up to " + price + " without the 10% bonus.")
