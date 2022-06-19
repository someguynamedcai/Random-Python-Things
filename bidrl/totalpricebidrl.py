#Testing how to find the total price for an item at bidrl.com
total = 0
price = 1
counter = 1
allitems = 0
file1 = open("TotalPaidBidrl.txt","w")
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
        print ("For all " + str(counter) + " items paid it is " + str(allitems) + ".\n")
        counter += 1
        file1.write(str(total))
    except:
        print ("Invalid input. Try again")

