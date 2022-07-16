#Attempt at mouse automation
import mouse

print ("Mouse recording started. To end the recording press the right mouse button inside the box.")
mouse.on_click(lambda: print("Left Button clicked."))
events = mouse.record()

print ("Completed recording.")
loop = int(input("How many times would you like to repeat these actions: "))

for count in range(loop):
    mouse.play(events[:-1])
    print ("Completed loop " + str(count + 1) + ".")
mouse.unhook_all()
done = input("Completed mouse playback.")
