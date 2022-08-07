#AS of 6/15/2022 This is only useful for games auctions as the owners of the website do not give enough detail on items. For games it is easy to search for just by title

import json
import requests
import webbrowser
import re
import time

print ("The following locations are: Sacramento, Elk Grove, Rancho Cordova, Citrus Heights, Natomas, Galt, and East Sacramento. \nPlease wait while the auction information is being loaded.")

#Spage = requests.get("https://www.bidrl.com/api/landingPage/sacramento-2")
Spage = requests.get("https://www.bidrl.com/api/landingPage/cesar-lua-2")
Sjson = Spage.json()
Epage = requests.get("https://www.bidrl.com/api/landingPage/elk-grove-8")
Ejson = Epage.json()
Rpage = requests.get("https://www.bidrl.com/api/landingPage/rancho-cordova-34")
Rjson = Rpage.json()
Cpage = requests.get("https://www.bidrl.com/api/landingPage/citrus-heights-37")
Cjson = Cpage.json()
Npage = requests.get("https://www.bidrl.com/api/landingPage/natomas-39")
Njson = Npage.json()
Gpage = requests.get("https://www.bidrl.com/api/landingPage/galt-7")
Gjson = Gpage.json()
ESpage = requests.get("https://www.bidrl.com/api/landingPage/east-sacramento-45")
ESjson = ESpage.json()

#Json page which has all auction item information
getitems = "https://www.bidrl.com/api/getitems"
cccprice = "https://camelcamelcamel.com/search?sq="
auctionlink = "bidrl.com/auction/"
edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

#Finding out the auction id of most recent gallery" that is not closed
for Sauctions in Sjson['auctions'].keys():
    if Sjson['auctions'][Sauctions]['status'] == "open":
        S_Id = Sjson['auctions'][Sauctions]['id']
        break
    
#Elk Grove Json page is not a dictionary but a list for some reason
for Eauctions in range(len(Ejson['auctions'])):
    if (Ejson['auctions'][Eauctions]['status'] == "open"):
        E_Id = Ejson['auctions'][Eauctions]['id']
        break
    
for Rauctions in Rjson['auctions'].keys():   
    if Rjson['auctions'][Rauctions]['status'] == "open":
        R_Id = Rjson['auctions'][Rauctions]['id']
        break
        
for Cauctions in Cjson['auctions'].keys():
    if Cjson['auctions'][Cauctions]['status'] == "open":
        C_Id = Cjson['auctions'][Cauctions]['id']
        break

for Nauctions in Njson['auctions'].keys():    
    if Njson['auctions'][Nauctions]['status'] == "open":
        N_Id = Njson['auctions'][Nauctions]['id']
        break

for Gauctions in Gjson['auctions'].keys():    
    if Gjson['auctions'][Gauctions]['status'] == "open":
        G_Id = Gjson['auctions'][Gauctions]['id']
        break
    
for ESauctions in range(len(ESjson['auctions'])):
    if (ESjson['auctions'][str(ESauctions+1)]['status'] == "open"):
        ES_Id = ESjson['auctions'][str(ESauctions+1)]['id']
        break

#Putting it into format for POST to getitems json page
SItems = {"auction_id": S_Id, "filters[perpage]": Sjson['auctions']['2']['item_count'] }
EItems = {"auction_id": E_Id, "filters[perpage]": Ejson['auctions'][0]['item_count']}
RItems = {"auction_id": R_Id, "filters[perpage]": Rjson['auctions']['1']['item_count']}
CItems = {"auction_id": C_Id, "filters[perpage]": Cjson['auctions']['1']['item_count']}
NItems = {"auction_id": N_Id, "filters[perpage]": Njson['auctions']['1']['item_count']}
GItems = {"auction_id": G_Id, "filters[perpage]": Gjson['auctions']['3']['item_count']}
ESItems = {"auction_id": ES_Id, "filters[perpage]": ESjson['auctions']['1']['item_count']}


#Retrieves item information from most recent gallery"
SPost = requests.post(getitems, data = SItems).json()
EPost = requests.post(getitems, data = EItems).json()
RPost = requests.post(getitems, data = RItems).json()
CPost = requests.post(getitems, data = CItems).json()
NPost = requests.post(getitems, data = NItems).json()
GPost = requests.post(getitems, data = GItems).json()
ESPost = requests.post(getitems, data = ESItems).json()



SItem1 = SPost['items'][0]['title']
EItem1 = EPost['items'][0]['title']
RItem1 = RPost['items'][0]['title']
CItem1 = CPost['items'][0]['title']
NItem1 = NPost['items'][0]['title']
GItem1 = GPost['items'][0]['title']
ESItem1 = ESPost['items'][0]['title']



Cleanquery = re.compile(re.escape('see pictures'), re.IGNORECASE)

def Itemcheck(location):
    while (True):
        try:
            print ("-------------------------------------------------------------------------------------------------------")
            number = input("Type in a number or type exit to go back to the previous prompt: ")
            number = str(number)
            if number == "exit" or number == "Exit":
                print ("Exiting current location.")
                return 
            else:
                match location:
                    case 'S':
                        print ("Item number " + number + " is titled " + SPost['items'][int(number)-1]['title'])
                        print ("The current price of item number " + number + " is $" + SPost['items'][int(number)-1]['current_bid'])
                        print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(SPost['items'][0]['current_bid']) * .0825 + float(SPost['items'][0]['current_bid']) + float(SPost['items'][0]['current_bid']) * .13))
                        cleanedq = Cleanquery.sub("", SPost['items'][int(number)-1]['title'])
                        Fulllink = cccprice + str(cleanedq)
                        Fullauctionlink = auctionlink + Sjson['auctions']['2']['id'] + "/item/" + SPost['items'][int(number)-1]['id']                                                                     
                        print ("A camelcamelcamel page and a page to the item will open in 2 seconds.")
                        time.sleep(2)
                        webbrowser.get('edge').open(Fulllink)
                        webbrowser.get('edge').open(Fullauctionlink)                                                                               
                    case 'E':
                        print ("Item number " + number + " is titled " + EPost['items'][int(number)-1]['title'])
                        print ("The current price of item number " + number + " is $" + EPost['items'][int(number)-1]['current_bid'])
                        print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(EPost['items'][0]['current_bid']) * .0825 + float(EPost['items'][0]['current_bid']) + float(EPost['items'][0]['current_bid']) * .13))
                        cleanedq = Cleanquery.sub("", EPost['items'][int(number)-1]['title'])
                        Fulllink = cccprice + str(cleanedq)
                        Fullauctionlink = auctionlink + Ejson['auctions'][2]['id'] + "/item/" + EPost['items'][int(number)-1]['id']                                                                     
                        print ("A camelcamelcamel page and a page to the item will open in 2 seconds.")
                        time.sleep(2)
                        webbrowser.get('edge').open(Fulllink)
                        webbrowser.get('edge').open(Fullauctionlink)                                                                               
                    case 'R':
                        print ("Item number " + number + " is titled " + RPost['items'][int(number)-1]['title'])
                        print ("The current price of item number " + number + " is $" + RPost['items'][int(number)-1]['current_bid'])
                        print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(RPost['items'][0]['current_bid']) * .0825 + float(RPost['items'][0]['current_bid']) + float(RPost['items'][0]['current_bid']) * .13))
                        cleanedq = Cleanquery.sub("", RPost['items'][int(number)-1]['title'])
                        Fulllink = cccprice + str(cleanedq)
                        Fullauctionlink = auctionlink + Rjson['auctions']['2']['id'] + "/item/" + RPost['items'][int(number)-1]['id']                                                                     
                        print ("A camelcamelcamel page and a page to the item will open in 2 seconds.")
                        time.sleep(2)
                        webbrowser.get('edge').open(Fulllink)
                        webbrowser.get('edge').open(Fullauctionlink)
                    case 'C':
                        print ("Item number " + number + " is titled " + CPost['items'][int(number)-1]['title'])
                        print ("The current price of item number " + number + " is $" + CPost['items'][int(number)-1]['current_bid'])
                        print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(CPost['items'][0]['current_bid']) * .0825 + float(CPost['items'][0]['current_bid']) + float(CPost['items'][0]['current_bid']) * .13))
                        cleanedq = Cleanquery.sub("", CPost['items'][int(number)-1]['title'])
                        Fulllink = cccprice + str(cleanedq)
                        Fullauctionlink = auctionlink + Cjson['auctions']['2']['id'] + "/item/" + CPost['items'][int(number)-1]['id']                                                                     
                        print ("A camelcamelcamel page and a page to the item will open in 2 seconds.")
                        time.sleep(2)
                        webbrowser.get('edge').open(Fulllink)
                        webbrowser.get('edge').open(Fullauctionlink)
                    case 'N':
                        print ("Item number " + number + " is titled " + NPost['items'][int(number)-1]['title'])
                        print ("The current price of item number " + number + " is $" + NPost['items'][int(number)-1]['current_bid'])
                        print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(NPost['items'][0]['current_bid']) * .0825 + float(NPost['items'][0]['current_bid']) + float(NPost['items'][0]['current_bid']) * .13))
                        cleanedq = Cleanquery.sub("", NPost['items'][int(number)-1]['title'])
                        Fulllink = cccprice + str(cleanedq)
                        Fullauctionlink = auctionlink + Njson['auctions']['2']['id'] + "/item/" + NPost['items'][int(number)-1]['id']                                                                     
                        print ("A camelcamelcamel page and a page to the item will open in 2 seconds.")
                        time.sleep(2)
                        webbrowser.get('edge').open(Fulllink)
                        webbrowser.get('edge').open(Fullauctionlink)
                    case 'G':
                        print ("Item number " + number + " is titled " + GPost['items'][int(number)-1]['title'])
                        print ("The current price of item number " + number + " is $" + GPost['items'][int(number)-1]['current_bid'])
                        print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(GPost['items'][0]['current_bid']) * .0825 + float(GPost['items'][0]['current_bid']) + float(GPost['items'][0]['current_bid']) * .13))
                        cleanedq = Cleanquery.sub("", GPost['items'][int(number)-1]['title'])
                        Fulllink = cccprice + str(cleanedq)
                        Fullauctionlink = auctionlink + Gjson['auctions']['3']['id'] + "/item/" + GPost['items'][int(number)-1]['id']                                                                     
                        print ("A camelcamelcamel page and a page to the item will open in 2 seconds.")
                        time.sleep(2)
                        webbrowser.get('edge').open(Fulllink)
                        webbrowser.get('edge').open(Fullauctionlink)
                    case 'ES':
                        print ("Item number " + number + " is titled " + ESPost['items'][int(number)-1]['title'])
                        print ("The current price of item number " + number + " is $" + ESPost['items'][int(number)-1]['current_bid'])
                        print ("The total price calculated with the 8.25% tax and 13% buyer's premium is $" + str(float(ESPost['items'][0]['current_bid']) * .0825 + float(ESPost['items'][0]['current_bid']) + float(ESPost['items'][0]['current_bid']) * .13))
                        cleanedq = Cleanquery.sub("", ESPost['items'][int(number)-1]['title'])
                        Fulllink = cccprice + str(cleanedq)
                        Fullauctionlink = auctionlink + ESjson['auctions']['2']['id'] + "/item/" + ESPost['items'][int(number)-1]['id']                                                                     
                        print ("A camelcamelcamel page and a page to the item will open in 2 seconds.")
                        time.sleep(2)
                        webbrowser.get('edge').open(Fulllink)
                        webbrowser.get('edge').open(Fullauctionlink)

        except IndexError:
            print ("The item number is invalid. Please type another number.")


Redirectto = input("\nPlease type a location to go to or type in 'Exit' to exit: ")
while Redirectto != "No":
    if (Redirectto == "Sacramento" or Redirectto == "sacramento" or Redirectto == 's' or Redirectto == 'S'):
        print ("The first auction gallery in Sacramento is a " + (Sjson['auctions']['2']['title']))
        print ("There are " + Sjson['auctions']['2']['item_count'] + " items in this gallery")
        Itemcheck("S")
    elif (Redirectto == "Exit" or Redirectto == "exit"):
        print ("Exiting program")
        break
    elif (Redirectto == "Elk Grove" or Redirectto == "elk grove" or Redirectto == "elkgrove" or Redirectto == "Elkgrove" or Redirectto == 'e' or Redirectto == 'E'):
        print ("The first auction gallery in Elk Grove is a " + (Ejson['auctions'][0]['title']))
        print ("There are " + Ejson['auctions'][1]['item_count'] + " items in this gallery.")
        Itemcheck("E")
        
    elif (Redirectto == "Rancho Cordova" or Redirectto == "rancho cordova" or Redirectto == "ranchocordova" or Redirectto == "Ranchocordova" or Redirectto == 'r' or Redirectto == 'R'):
        print ("The first auction gallery in Rancho Cordova is a " + (Rjson['auctions']['1']['title']))
        print ("There are " + Rjson['auctions']['1']['item_count'] + " items in this gallery.")
        Itemcheck("R")
        
    elif (Redirectto == "Citrus Heights" or Redirectto == "citrus heights" or Redirectto == "citrusheights" or Redirectto == "Citrusheights" or Redirectto == 'C' or Redirectto == 'c'):
        print ("The first auction gallery in Citrus Heights is a " + (Cjson['auctions']['1']['title']))
        print ("There are " + Cjson['auctions']['1']['item_count'] + " items in this gallery.")
        Itemcheck("C")
        
    elif (Redirectto == "Natomas" or Redirectto == "natomas" or Redirectto == 'n' or Redirectto == 'N'):
        print ("The first auction gallery in Natomas is a " + (Njson['auctions']['1']['title']))
        print ("There are " + Njson['auctions']['1']['item_count'] + " items in this gallery.")
        Itemcheck("N")
               
    elif (Redirectto == "Galt" or Redirectto == "galt" or Redirectto == 'g' or Redirectto == 'G'):
        print ("The first auction gallery in Galt is a " + (Gjson['auctions']['3']['title']))
        print ("There are " + Gjson['auctions']['3']['item_count'] + " items in this gallery.")
        Itemcheck("G")
    elif (Redirectto == "East Sacramento" or Redirectto == "east sacramento" or Redirectto == 'es' or Redirectto == 'ES' or Redirectto == 'Es' or Redirectto == 'east' or Redirectto == 'East'):
        print ("The first auction gallery in East Sacramento is a " + (ESjson['auctions']['1']['title']))
        print ("There are " + ESjson['auctions']['1']['item_count'] + " items in this gallery.")
        Itemcheck("ES")
    else:
        print("Keyword not valid or recognized. Please type again:")
    print ("The following locations are: Sacramento, Elk Grove, Rancho Cordova, Citrus Heights, Natomas, Galt, and East Sacramento.")
    Redirectto = input("\nPlease type a location to go to or type in 'Exit' to exit: ")
