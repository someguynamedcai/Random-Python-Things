import webbrowser


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
    webbrowser.open('https://steamcharts.com/search/?q='+ query)



