from urllib.request import Request, urlopen
gameurl = ""
playercount = 0

while (True):
    game = (input("Type in an game to see Steamcharts stats or type Exit to exit: "))
    if (game == "Exit" or game == "exit"):
        break
    gamelist = game.split()
    query = ""

    for num in gamelist:
        query = (query + num + "+")
    query = query.rstrip(query[-1])
    print ("Searching for the game " + game + " in Steamcharts.")
    gameurl = ("https://steamcharts.com/search/?q=" + query)
    req = Request(gameurl, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    html = webpage.decode("utf-8")
    playerfind = html.find("right num")
    playercount = html[playerfind+11:playerfind+17]
    print (playercount)
    print (playercount.isalpha())
    if (playercount.isalpha() == True):
        print ("Steamcharts could not find any results for your search. Please try again.")
    elif playercount == "0":
        print ("Steamcharts sees there are zero players. You may have typed your query wrong in some cases.") 
    else:   
        print ("Steamcharts indicates there are " + playercount + " players currently playing the game right now.")





