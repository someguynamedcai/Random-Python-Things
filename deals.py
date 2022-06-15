import webbrowser

item = (input("Type in an item: "))
itemlist = item.split()
product = ""

for num in itemlist:
    product = (product + num + "+")
product = product.rstrip(product[-1])

print ("Looking for " + item + " deals and searches.")

webbrowser.open('https://slickdeals.net/newsearch.php?q='+ product)
webbrowser.open_new_tab("https://www.amazon.com/s?k=" + product)
webbrowser.open_new_tab("https://brickseek.com/products/?search=" +product)
webbrowser.open_new_tab("https://www.bidrl.com/allitems/keyword_" +product)




