#Web scraping the site bidrl 
import os
import json
import requests
import datetime
import time
import webbrowser
print ("Information is being obtained from BidRL. Please wait for a moment.")

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
ROpage = requests.get("https://www.bidrl.com/api/landingPage/roseville-48")
ROjson = ROpage.json()
os.system("cls")
#Json page which has all auction item information

getitems = "https://www.bidrl.com/api/getitems"


#In use when a gallery is only 1 item
def Oneitem(location,ID,number):
    if (location == "R"):
        currentunixtime = time.time()
        RPost = requests.post("https://www.bidrl.com/api/ItemData", data = {"item_id": ID,}).json()
        RItemtime = float(RPost['end_time']) + 7200
        Rtimeleft = RItemtime - currentunixtime
        Rtimes = Rjson['auctions'][str(number)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        print ("This item will close in " + str(datetime.timedelta(seconds = Rtimeleft)))        
        print (Rtimes)
        print ("------------------------------------------------------------------------------------------------------------------------------")

#Printing info on locations
  
def Einfo(currenttime,currentunixtime):
    try:
        for Eauctions in range(len(Ejson['auctions'])):
            if (Ejson['auctions'][(Eauctions)]['status'] == "open" and Ejson['auctions'][(Eauctions)]['item_id'] != "null"):
                E_Id = Ejson['auctions'][(Eauctions)]['id']
                Efirst = Eauctions
                break
    except (KeyError):
        for Eauctions in Ejson['auctions'].keys():
            if (Ejson['auctions'][(Eauctions)]['status'] == "open" and Ejson['auctions'][(Eauctions)]['item_id'] != "null"):
                E_Id = Ejson['auctions'][(Eauctions)]['id']
                Efirst = Eauctions
                break
    except (NameError, AttributeError):
        print("There are no open auctions in Elk Grove as of this moment.\n")
    try:
        EItems = {"auction_id": E_Id,}
        EPost = requests.post(getitems, data = EItems).json()
        EItem1 = EPost['items'][0]['title']
        Etimes = Ejson['auctions'][(Eauctions)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        EItemtime = float(EPost['items'][0]['ends']) + 7200
        Etimeleft = EItemtime - currentunixtime
            
        if Etimes.find("First Item Closes") != -1:
            print ("The first auction gallery in Elk Grove is a " + (Ejson['auctions'][(Eauctions)]['title']))
            if (Etimeleft < 0):
                print ("The current gallery is closing items right now!")
            else:
                print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Etimeleft)))
                print(Etimes)
            print ("------------------------------------------------------------------------------------------------------------------------------")
        else:
            Etimes = Ejson['auctions'][(int(Eauctions)+1)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
            print ("An auction has recently closed. The next auction gallery in Elk Grove is a " + (Ejson['auctions'][(int(Eauctions)+1)]['title']))
            print ("------------------------------------------------------------------------------------------------------------------------------")
        return Eauctions
    except (NameError,AttributeError,UnboundLocalError):
        print ("THERE ARE NO OPEN AUCTIONS IN ELK GROVE RIGHT NOW.")
        print ("------------------------------------------------------------------------------------------------------------------------------")
        
def Rinfo(currenttime,currentunixtime):
    try:
        for Rauctions in range(len(Rjson['auctions'])):   
            if Rjson['auctions'][Rauctions]['status'] == "open":
                R_Id = Rjson['auctions'][Rauctions]['id']
                break
    except (KeyError):
        for Rauctions in Rjson['auctions'].keys():   
            if Rjson['auctions'][Rauctions]['status'] == "open":
                R_Id = Rjson['auctions'][Rauctions]['id']
                break
    except (NameError,AttributeError):
        print ("There are no open auctions in Rancho Cordova as of this moment.\n")
    try:    
        RItems = {"auction_id": R_Id,}
        RPost = requests.post(getitems, data = RItems).json()
        RItem1 = RPost['items'][0]['title']
        Rtimes = Rjson['auctions'][str(Rauctions)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        RItemtime = float(RPost['items'][0]['ends']) + 7200
        Rtimeleft = RItemtime - currentunixtime
        Rauctionlink = Rjson['auctions'][Rauctions]['id'] + "/item/" + Rjson['auctions'][Rauctions]['item_id_slug']
            
        if Rtimes.find("First Item Closes") != -1 or Rtimes.find("Closing Time") != -1:
            print ("The first auction gallery in Rancho Cordova is a " + (Rjson['auctions'][str(Rauctions)]['title']))
            if (Rjson['auctions'][Rauctions]['item_count'] == "1"):
                Oneitem("R",Rjson['auctions'][Rauctions]['item_id'],Rauctions)
            else:
                if (Rtimeleft < 0):
                    print ("The current gallery is closing items right now!")
                else:
                    print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Rtimeleft)))
                    print(Rtimes)
                print ("------------------------------------------------------------------------------------------------------------------------------")
        else:
            Rtimes = Rjson['auctions'][str(int(Rauctions)+1)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
            print ("An auction has recently closed. The next auction gallery in Rancho Cordova is a " + (Rjson['auctions'][str(int(Rauctions)+1)]['title']))
            print ("------------------------------------------------------------------------------------------------------------------------------")
        return Rauctions
    except (NameError,AttributeError,UnboundLocalError):
        print ("THERE ARE NO OPEN AUCTIONS IN RANCHO CORDOVA RIGHT NOW.")
        print ("------------------------------------------------------------------------------------------------------------------------------")
        

def Cinfo(currenttime,currentunixtime):
    try: 
        for Cauctions in range(len(Cjson['auctions'])):
            if Cjson['auctions'][Cauctions]['status'] == "open":
                C_Id = Cjson['auctions'][Cauctions]['id']
                break
    except (KeyError):
        for Cauctions in Cjson['auctions'].keys():
            if Cjson['auctions'][Cauctions]['status'] == "open":
                C_Id = Cjson['auctions'][Cauctions]['id']
                break
    try:
        CItems = {"auction_id": C_Id,}
        CPost = requests.post(getitems, data = CItems).json()
        CItem1 = CPost['items'][0]['title']
        Ctimes = Cjson['auctions'][Cauctions]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        CItemtime = float(CPost['items'][0]['ends']) + 7200
        Ctimeleft = CItemtime - currentunixtime
        
        if Ctimes.find("First Item Closes") != -1:
            print ("The first auction gallery in Citrus Heights is a " + (Cjson['auctions'][str(Cauctions)]['title']))
            if (Ctimeleft < 0):
                print ("The current gallery is closing items right now!")
            else:
                print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Ctimeleft)))
                print(Ctimes)
            print ("------------------------------------------------------------------------------------------------------------------------------")
        else:
            Ctimes = Cjson['auctions'][str(int(Cauctions)+1)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
            print ("An auction has recently closed. The next auction gallery in Citrus Heights is a " + (Cjson['auctions'][str(int(Cauctions)+1)]['title']))
            print ("------------------------------------------------------------------------------------------------------------------------------")
        return Cauctions
    except (NameError,AttributeError,UnboundLocalError):
        print ("THERE ARE NO OPEN AUCTIONS IN CITRUS HEIGHTS RIGHT NOW.")
        print ("------------------------------------------------------------------------------------------------------------------------------")
        
def Ninfo(currenttime,currentunixtime):
    try:
        for Nauctions in range(len(Njson['auctions'])):
            if Njson['auctions'][Nauctions]['status'] == "open" and Njson['auctions'][(Nauctions)]['item_id'] != "null":
                N_Id = Njson['auctions'][Nauctions]['id']
                break
    except (KeyError):
        for Nauctions in Njson['auctions'].keys():
            if Njson['auctions'][Nauctions]['status'] == "open" and Njson['auctions'][(Nauctions)]['item_id'] != "null":
                N_Id = Njson['auctions'][Nauctions]['id']
                break
    try:        
        NItems = {"auction_id": N_Id,}
        NPost = requests.post(getitems, data = NItems).json()
        NItem1 = NPost['items'][0]['title']
        Ntimes = Njson['auctions'][Nauctions]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        NItemtime = float(NPost['items'][0]['ends']) + 7200
        Ntimeleft = NItemtime - currentunixtime
        
        if Ntimes.find("First Item Closes") != -1:
            print ("The first auction gallery in Natomas is a " + (Njson['auctions'][(Nauctions)]['title']))
            if (Ntimeleft < 0):
                print ("The current gallery is closing items right now!")
            else :    
                print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Ntimeleft)))
                print(Ntimes)
            print ("------------------------------------------------------------------------------------------------------------------------------")
        else:
            Ntimes = Njson['auctions'][str(int(Nauctions)+1)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
            print ("An auction has recently closed. The next auction gallery in Natomas is a " + str(Njson['auctions'][str(int(Sauctions)+1)]['title']))
            print ("------------------------------------------------------------------------------------------------------------------------------")
        return Nauctions
    
    except (NameError,AttributeError,UnboundLocalError):
        print ("THERE ARE NO OPEN AUCTIONS IN NATOMAS RIGHT NOW.")
        print ("------------------------------------------------------------------------------------------------------------------------------")
        
def Ginfo(currenttime,currentunixtime):
    try:
        for Gauctions in range(len(Gjson['auctions'])):
            if Gjson['auctions'][Gauctions]['status'] == "open" and "coming-soon" not in Gjson['auctions'][Gauctions]['item_id_slug']:
                G_Id = Gjson['auctions'][Gauctions]['id']
                break
    except (KeyError):
        for Gauctions in Gjson['auctions'].keys():
            if Gjson['auctions'][Gauctions]['status'] == "open" and Gjson['auctions'][(Gauctions)]['item_id'] != "null" and "coming-soon" not in Gjson['auctions'][Gauctions]['item_id_slug']:
                G_Id = Gjson['auctions'][Gauctions]['id']
                break
    try:    
        GItems = {"auction_id": G_Id,}
        GPost = requests.post(getitems, data = GItems).json()
        GItem1 = GPost['items'][0]['title']
        Gtimes = Gjson['auctions'][Gauctions]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        GItemtime = float(GPost['items'][0]['ends']) + 7200
        Gtimeleft = GItemtime - currentunixtime
        if Gtimes.find("Closing Time") != -1 or Gtimes.find("First Item Closes") != -1:
            print ("The first auction gallery in Galt is a " + (Gjson['auctions'][str(Gauctions)]['title']))
            if (Gtimeleft < 0):
                print ("The current gallery is closing items right now!")
            else :    
                print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = Gtimeleft)))
                print(Gtimes)
            print ("------------------------------------------------------------------------------------------------------------------------------")
        else:
            Gtimes = Gjson['auctions'][str(int(Gauctions)+1)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
            print ("An auction has recently closed. The next auction gallery in Galt is a " + (Gjson['auctions'][str(int(Gauctions)+1)]['title']))
            print ("------------------------------------------------------------------------------------------------------------------------------")
        return Gauctions
    except (NameError,AttributeError,UnboundLocalError):
        print ("THERE ARE NO OPEN AUCTIONS IN GALT RIGHT NOW.")
        print ("------------------------------------------------------------------------------------------------------------------------------")
        
def ESinfo(currenttime,currentunixtime):
    try:    
        for ESauctions in range(len(ESjson['auctions'])):
            if (ESjson['auctions'][ESauctions]['status'] == "open"):
                ES_Id = ESjson['auctions'][ESauctions]['id']
                break
    except (KeyError):
        for ESauctions in ESjson['auctions'].keys():
            if (ESjson['auctions'][ESauctions]['status'] == "open"):
                ES_Id = ESjson['auctions'][ESauctions]['id']
                break
    try:
        ESItems = {"auction_id": ES_Id,}
        ESPost = requests.post(getitems, data = ESItems).json()
        ESItem1 = ESPost['items'][0]['title']
        EStimes = ESjson['auctions'][ESauctions]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        ESItemtime = float(ESPost['items'][0]['ends']) + 7200
        EStimeleft = ESItemtime - currentunixtime

        if EStimes.find("First Item Closes") != -1:
            print ("The first auction gallery in East Sacramento is a " + (ESjson['auctions'][(ESauctions)]['title']))
            if (EStimeleft < 0):
                print ("The current gallery is closing items right now!")
            else:
                print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = EStimeleft)))
                print(EStimes)
            print ("------------------------------------------------------------------------------------------------------------------------------")
        else:
            EStimes = ESjson['auctions'][str(int(ESauctions)+1)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
            print ("An auction has recently closed. The next auction gallery in East Sacramento is a " + (ESjson['auctions'][str(int(ESauctions)+1)]['title']))
            print ("------------------------------------------------------------------------------------------------------------------------------")
        return ESauctions
    except (NameError,AttributeError,UnboundLocalError):
        print ("THERE ARE NO OPEN AUCTIONS IN EAST SACRAMENTO RIGHT NOW.")
        print ("------------------------------------------------------------------------------------------------------------------------------")
        

def ROinfo(currenttime,currentunixtime):
    try:
        for ROauctions in range(len(ROjson['auctions'])):
            if ROjson['auctions'][ROauctions]['status'] == "open":
                RO_Id = ROjson['auctions'][ROauctions]['id']
                break
    except (KeyError):
        for ROauctions in ROjson['auctions'].keys():
            if ROjson['auctions'][ROauctions]['status'] == "open":
                RO_Id = ROjson['auctions'][ROauctions]['id']
                break
    
    try:    
        ROItems = {"auction_id": RO_Id,}
        ROPost = requests.post(getitems, data = ROItems).json()
        ROItem1 = ROPost['items'][0]['title']
        ROtimes = ROjson['auctions'][(ROauctions)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
        ROItemtime = float(ROPost['items'][0]['ends']) + 7200
        ROtimeleft = ROItemtime - currentunixtime
        ROauctionlink = ROjson['auctions'][ROauctions]['id'] + "/item/" + ROjson['auctions'][ROauctions]['item_id_slug']
        
        if ROtimes.find("First Item Closes") != -1 or ROtimes.find("Closing Time") != -1:
            print ("The first auction gallery in Roseville is a " + (ROjson['auctions'][(ROauctions)]['title']))
            if (ROjson['auctions'][ROauctions]['item_count'] == "1"):
                Oneitem("R",ROjson['auctions'][ROauctions]['item_id'])
            else:
                if (ROtimeleft < 0):
                    print ("The current gallery is closing items right now!")
                else:
                    print ("The first item in this gallery will close in " + str(datetime.timedelta(seconds = ROtimeleft)))
                    print(ROtimes)
                print ("------------------------------------------------------------------------------------------------------------------------------")
        else:
            ROtimes = ROjson['auctions'][(int(ROauctions)+1)]['info_div'].replace("<b>","").replace("</b>"," ").replace("<br>","").replace("<br />"," ")
            print ("An auction has recently closed. The next auction gallery in Roseville is a " + (ROjson['auctions'][(int(ROauctions)+1)]['title']))
            print ("------------------------------------------------------------------------------------------------------------------------------")
        return ROauctions
    except (NameError,AttributeError,UnboundLocalError):
        print ("THERE ARE NO OPEN AUCTIONS IN ROSEVILLE RIGHT NOW.")
        print ("------------------------------------------------------------------------------------------------------------------------------")
          
#Finding out where edge is located on computer to open web page
#Default path to Edge, may not work for everyone
edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

Startlink = "https://www.bidrl.com/auction/"

def main():
    #Current date and time
    currenttime = datetime.datetime.now()
    currentunixtime = time.time()
    print ("Today is " + str(currenttime.date()) + ".\nThe time is " + str(currenttime.strftime("%H:%M:%S")) + ".\n")
    #print ("There are " + str(Sjson['total']) + " auction galleries available at Sacramento.")
    print ("There are " + str(Ejson['total']) + " auction galleries available at Elk Grove.")
    print ("There are " + str(Rjson['total']) + " auction galleries available at Rancho Cordova.")
    print ("There are " + str(Cjson['total']) + " auction galleries available at Citrus Heights.")
    print ("There are " + str(Njson['total']) + " auction galleries available at Natomas.")
    print ("There are " + str(Gjson['total']) + " auction galleries available at Galt.")
    print ("There are " + str(ESjson['total']) + " auction galleries available at East Sacramento.")
    print ("There are " + str(ROjson['total']) + " auction galleries available at Roseville.")
    print ("------------------------------------------------------------------------------------------------------------------------------")
    #Sfirst = Sinfo(currenttime,currentunixtime)
    Eauctions = Einfo(currenttime,currentunixtime)
    Rauctions = Rinfo(currenttime,currentunixtime)
    Cauctions = Cinfo(currenttime,currentunixtime)
    Nauctions = Ninfo(currenttime,currentunixtime)
    Gauctions = Ginfo(currenttime,currentunixtime)
    ESauctions = ESinfo(currenttime,currentunixtime)
    ROauctions = ROinfo(currenttime,currentunixtime)

#Input to open web page to auction gallery            
    Redirectto = input("Please type a location to go to or type in 'Exit' to exit: ")
    while Redirectto != "No":
        try:
            '''if (Redirectto == "Sacramento" or Redirectto == "sacramento" or Redirectto == 's' or Redirectto == 'S'):
                print ("Opening up the most recent Sacramento gallery.\n")
                Fulllink = Startlink + Sjson['auctions'][Sfirst]['auction_id_slug']
                webbrowser.get('edge').open(Fulllink)'''
            if (Redirectto == "Exit" or Redirectto == "exit" or Redirectto == "Close" or Redirectto == "close" or Redirectto == "quit" or Redirectto == "Quit"):
                print ("Exiting program")
                break
            elif (Redirectto == "Elk Grove" or Redirectto == "elk grove" or Redirectto == "elkgrove" or Redirectto == "Elkgrove" or Redirectto == 'e' or Redirectto == 'E'):
                print ("Opening up the most recent Elk Grove gallery.\n")
                Fulllink = Startlink + Ejson['auctions'][Eauctions]['auction_id_slug']
                webbrowser.get('edge').open(Fulllink)
            elif (Redirectto == "Rancho Cordova" or Redirectto == "rancho cordova" or Redirectto == "ranchocordova" or Redirectto == "Ranchocordova" or Redirectto == 'r' or Redirectto == 'R' or Redirectto == "Rancho" or Redirectto == "rancho"):
                print ("Opening up the most recent Rancho Cordova gallery.\n")
                Fulllink = Startlink + Rjson['auctions'][Rauctions]['auction_id_slug']
                webbrowser.get('edge').open(Fulllink)
            elif (Redirectto == "Citrus Heights" or Redirectto == "citrus heights" or Redirectto == "citrusheights" or Redirectto == "Citrusheights" or Redirectto == 'C' or Redirectto == 'c'):
                print ("Opening up the most recent Citrus Heights gallery.\n")
                Fulllink = Startlink + Cjson['auctions'][Cauctions]['auction_id_slug']
                webbrowser.get('edge').open(Fulllink)
            elif (Redirectto == "Natomas" or Redirectto == "natomas" or Redirectto == 'n' or Redirectto == 'N'):
                print ("Opening up the most recent Natomas gallery.\n")
                Fulllink = Startlink + Njson['auctions'][Nauctions]['auction_id_slug']
                webbrowser.get('edge').open(Fulllink)
            elif (Redirectto == "Galt" or Redirectto == "galt" or Redirectto == 'g' or Redirectto == 'G'):
                print ("Opening up the most recent Galt gallery.\n")
                Fulllink = Startlink + Gjson['auctions'][Gauctions]['auction_id_slug']
                webbrowser.get('edge').open(Fulllink)
            elif (Redirectto == "East Sacramento" or Redirectto == "east sacramento" or Redirectto == 'es' or Redirectto == 'ES' or Redirectto == 'Es' or Redirectto == 'east' or Redirectto == 'East'):
                print ("Opening up the most recent East Sacramento gallery.\n")
                try:
                    Fulllink = Startlink + ESjson['auctions'][ESauctions]['auction_id_slug']
                except TypeError:
                    Fulllink = "https://www.bidrl.com/affiliate/east-sacramento-45/"
                webbrowser.get('edge').open(Fulllink)
            elif (Redirectto == "Roseville" or Redirectto == "roseville" or Redirectto == 'ro' or Redirectto == 'RO' or Redirectto == 'Ro' or Redirectto == 'rose' or Redirectto == 'Rose'):
                print ("Opening up the most recent Roseville gallery.\n")
                try:
                    Fulllink = Startlink + ROjson['auctions'][ROauctions]['auction_id_slug']
                except TypeError:
                    Fulllink = "https://www.bidrl.com/affiliate/roseville/"
                webbrowser.get('edge').open(Fulllink)            
            elif (Redirectto == "refresh" or Redirectto == "Refresh" or Redirectto == "update" or Redirectto == "Update" or Redirectto == "restart" or Redirectto == "Restart"):
                print ("Updating information. Please wait.")
                main()
            else:
                print("Keyword not valid or recognized. Please type again:")
            Redirectto = input("Please type a location to go to or type in 'Exit' to exit: ")
        except KeyError:
            print ("There has been an error in opening up the gallery.")
            Redirectto = input("Please type a location to go to or type in 'Exit' to exit: ")

main()

