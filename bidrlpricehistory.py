import json
import requests
import datetime
import time
import webbrowser

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

#Json page which has all auction item information
getitems = "https://www.bidrl.com/api/getitems"

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
    
#Putting it into format for POST to getitems json page
SItems = {"auction_id": S_Id,}
EItems = {"auction_id": E_Id,}
RItems = {"auction_id": R_Id,}
CItems = {"auction_id": C_Id,}
NItems = {"auction_id": N_Id,}
GItems = {"auction_id": G_Id,}

#Retrieves item information from most recent gallery"
SPost = requests.post(getitems, data = SItems).json()
EPost = requests.post(getitems, data = EItems).json()
RPost = requests.post(getitems, data = RItems).json()
CPost = requests.post(getitems, data = CItems).json()
NPost = requests.post(getitems, data = NItems).json()
GPost = requests.post(getitems, data = GItems).json()


SItem1 = SPost['items'][0]['title']
EItem1 = EPost['items'][0]['title']
RItem1 = RPost['items'][0]['title']
CItem1 = CPost['items'][0]['title']
NItem1 = NPost['items'][0]['title']
GItem1 = GPost['items'][0]['title']

print ("The first item in the Sacramento gallery is " + SItem1)
print ("The first item in the Elk Grove gallery is " + EItem1)
print ("The first item in the Rancho Cordova gallery is " + RItem1)
print ("The first item in the Citrus Heights gallery is " + CItem1)
print ("The first item in the Natomas gallery is " + NItem1)
print ("The first item in the Galt gallery is " + GItem1)


Redirectto = input("\nPlease type a location to go to or type in 'Exit' to exit: ")
while Redirectto != "No":
    if (Redirectto == "Sacramento" or Redirectto == "sacramento" or Redirectto == 's' or Redirectto == 'S'):
        print ("The first auction gallery in Sacramento is a " + (Sjson['auctions']['1']['title']))
        print ("There are " + Sjson['auctions']['1']['item_count'] + " items in this gallery")
        
    elif (Redirectto == "Exit" or Redirectto == "exit"):
        print ("Exiting program")
        break
    elif (Redirectto == "Elk Grove" or Redirectto == "elk grove" or Redirectto == "elkgrove" or Redirectto == "Elkgrove" or Redirectto == 'e' or Redirectto == 'E'):
        print ("The first auction gallery in Elk Grove is a " + (Ejson['auctions'][0]['title']))
        print ("There are " + Ejson['auctions']['1']['item_count'] + " items in this gallery")
        
    elif (Redirectto == "Rancho Cordova" or Redirectto == "rancho cordova" or Redirectto == "ranchocordova" or Redirectto == "Ranchocordova" or Redirectto == 'r' or Redirectto == 'R'):
        print ("The first auction gallery in Rancho Cordova is a " + (Rjson['auctions']['1']['title']))
        print ("There are " + Rjson['auctions']['1']['item_count'] + " items in this gallery")
        
    elif (Redirectto == "Citrus Heights" or Redirectto == "citrus heights" or Redirectto == "citrusheights" or Redirectto == "Citrusheights" or Redirectto == 'C' or Redirectto == 'c'):
        print ("The first auction gallery in Citrus Heights is a " + (Cjson['auctions']['1']['title']))
        
    elif (Redirectto == "Natomas" or Redirectto == "natomas" or Redirectto == 'n' or Redirectto == 'N'):
        print ("The first auction gallery in Natomas is a " + (Njson['auctions']['1']['title']))
        print ("There are " + Njson['auctions']['1']['item_count'] + " items in this gallery")
               
    elif (Redirectto == "Galt" or Redirectto == "galt" or Redirectto == 'g' or Redirectto == 'G'):
        print ("The first auction gallery in Galt is a " + (Gjson['auctions']['2']['title']))
        print ("There are " + Gjson['auctions']['1']['item_count'] + " items in this gallery")
    else:
        print("Keyword not valid or recognized. Please type again:")
    Redirectto = input("Please type a location to go to or type in 'Exit' to exit: ")



#
