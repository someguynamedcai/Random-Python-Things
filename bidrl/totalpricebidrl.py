price = 1
while (price != 0):
    print ("What is the price:")
    price = float(input())

    if (price == 0):
        print ("Program End")
        break
    
    tax = price * (.1)
    premium = price * (.13)

    print ("\nThe tax (8%) paid is " + str(tax))
    print ("The premium (13%) paid is " + str(premium))
    print ("The total paid is " + (str(price + tax + premium)) + "\n")


