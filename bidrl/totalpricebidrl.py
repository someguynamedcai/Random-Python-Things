price = 1
while (price != 0):

    price = input("What is the price? (type exit to close program): ")

    if (price == "exit" or price == "Exit"):
        print ("Program End")
        break

    tax = float(price) * (.0825)
    premium = float(price) * (.13)

    print ("\nThe tax (8.25%) paid is " + str(tax))
    print ("The premium (13%) paid is " + str(premium))
    print ("The total paid is " + (str(float(price) + tax + premium)) + "\n")


