#Testing how to find the total price for an item at bidrl.com
import datetime
import os
import re

#All variables needed to calculate
total = 0
price = 1
counter = 0
totaltax = 0
totalpremium = 0
allitems = 0
allauctions = 0
currentdate = str(datetime.datetime.now())

historyfile = open("TotalPaidBidrl.txt","a+")

while (price != 0):
    try:
        price = input("What is the price of all items paid? (type exit or close to close program): ")

        if (price == "exit" or price == "Exit" or price == "close" or price == "Close"):
            break

        #Calculating and printing text
        tax = float(price) * (.0875)
        premium = float(price) * (.13)
        total = float(price) + tax + premium
        allitems = round(allitems + total,3)
        totaltax = round(totaltax + tax,3)
        totalpremium = round(totalpremium + premium,3)
        print ("\nThe tax (8.75%) paid is " + str(tax) + ".")
        print ("The premium (13%) paid is " + str(premium) + ".")
        print ("The total paid is " + (str(total) + "."))
        print ("\nThe total cost of tax for all items is " + str(totaltax))
        print ("The total cost of the premium for all items is " + str(totalpremium))
        print ("For all " + str(counter+1) + " items paid it is " + str(allitems) + ".")
        counter += 1
    except ValueError:
        print ("Invalid input. Try again")

#Will only write to file if a real price was added
if counter > 0:
        print ("Information has been written to TotalPaidBidrl.txt")
        #Not sure why it only writes to a new line with 2 \n compared to 1
        if os.stat("TotalPaidBidrl.txt").st_size > 0:
                historyfile.write("\n\nDate:" + currentdate + "\n")
        else:
               historyfile.write("Date:" + currentdate + "\n")
               allauctions = allauctions + allitems
        historyfile.write("Total: $" + str(allitems) + "\nItems: " + str(counter) + "\n")
        historyfile.write("Total Premium: $" + str(totalpremium) + " Total Tax: $" + str(totaltax) + "\n")
        with open('TotalPaidBidrl.txt') as pricefile:
                for line in pricefile:
                        if (line[0:12] == "Total of all"):
                                allauctions = allitems + float(line[26:32])
        historyfile.write("Total of all items paid: $" + str(round(allauctions,3)))
        historyfile.close()


