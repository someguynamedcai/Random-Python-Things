#Testing how to find the total price for an item at bidrl.com
import datetime
import os
import re

total = 0
price = 1
counter = 0
allitems = 0
currentdate = str(datetime.datetime.now())
print (currentdate)
historyfile = open("TotalPaidBidrl.txt","a+")
if os.stat("TotalPaidBidrl.txt").st_size > 0:
        historyfile.write("\nDate:" + currentdate + "\n")
else:
        historyfile.write("Date:" + currentdate + "\n")
        
while (price != 0):
    try:
        price = input("What is the price? (type exit to close program): ")

        if (price == "exit" or price == "Exit"):
            print ("Program End")
            break

        tax = float(price) * (.0825)
        premium = float(price) * (.13)
        total = float(price) + tax + premium
        allitems = allitems + total
        print ("\nThe tax (8.25%) paid is " + str(tax) + ".")
        print ("The premium (13%) paid is " + str(premium) + ".")
        print ("The total paid is " + (str(total) + "."))
        print ("For all " + str(counter+1) + " items paid it is " + str(allitems) + ".")
        counter += 1
    except:
        print ("Invalid input. Try again")
        
historyfile.write("Total:$" + str(allitems) + " Items: " + str(counter) + "\n")

histryofile. 
historyfile.close()

