import webbrowser
import random
import time
import os

counter = 0

#path to edge app
edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

#format for search
startquery = "https://www.bing.com/search?q="

#dictionary for random words and counter 
searchwords = ["amazon","2022","2021","google","weather","news","steam","facebook","youtube","monday",
               "tuesday","wednesday","thursday","friday","saturday","sunday","today","yesterday","stock","ebay",
               "brickseek","bidrl","reddit","bitcoin","gamestop","birthday","holiday","nba","nfl","US",
               "EU","ethereum","indeed","jobs","duckduckgo","google play","app store","walmart","target","best buy",
               "black friday","christmas","new year","lunar","steam sale","slickdeals","microsoft store","gog","craigslist","cag",
               "psn","xbox","coinbase","salesforce","glassdoor","epic","wikipedia","imdb","amazon prime","hulu",
               "peacock","disney plus","gmail","outlook","teams","protonmail","fidelity","vanguard","netflix","paramount",
               "vudu","fandango","rotten tomatoes","humble bundle","fanatical","indiegala","gamesplanet","dlgamer","gamersgate","gamebillet",
               "crunchyroll","funimation","hbo","cnn","yahoo","apple tv","eshop","amazon luna","google stadia","game pass",
               "steamcharts","fortnite","apex legends", "local news","ziprecruiter","monster","careerbuilder","wheres waldo","spotify","pandora",
               "woot","chatgpt","stablediffusion", "nvidia drivers", "amd drivers","ai art","rakuten","walgreens"]

for x in range(36):
    randnum = random.randrange(len(searchwords))
    newsearch = startquery + searchwords[randnum]
    #Removes word so it doesn't repeat
    searchwords.pop(randnum)
    webbrowser.get('edge').open(newsearch)
    time.sleep(3)
    counter+=1
    print (str(x+1) + " searches have been completed.")

os.system('cls')
input("Completed " + str(counter) + " searches.")
os.system("taskkill /im msedge.exe /f")


