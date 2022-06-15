import webbrowser
StartLocation = (input("Type in a starting location: "))
StartList = StartLocation.split()
Destination = input("Type in a destination: ")
DestinationList = Destination.split()
Start = ""
End = ""
for num in StartList:
    Start = (Start + num + "+")
    
for num in DestinationList:
    End = (End + num + "+")

Start = Start.rstrip(Start[-1])
End = End.rstrip(End[-1])
webbrowser.open('https://www.google.com/maps/dir/'+ Start + "/" + End)



