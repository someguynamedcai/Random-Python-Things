from urllib.request import Request, urlopen
gameurl = ""
while (True):
    playercount = 0
    playercountfix = ""
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

    for count in range(len(playercount)):
        if playercount[count].isnumeric() == False:
            break
        playercountfix = playercountfix + (playercount[count])
    try:
        if (int(playercountfix) == 0):
            print ("Steamcharts sees there are zero players. You may have typed your query wrong in some cases.")
        elif int(playercountfix) > 0:
            print ("Steamcharts indicates there are " + playercountfix + " players currently playing the game right now.")
        else:   
            print ("Steamcharts could not find any results for your search. Please try again.")
    except ValueError:
        print ("The following game cannot be found. Please correct your search.")





