# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

# class Input(object):
#     def __init__

def init(data):
    data.string = "Enter Text Here"
    data.isPressed = False
    data.rectCoords = (data.width/2-100, data.height/2-20,data.width/2+100,
            data.height/2+20)
    data.textCoords = (data.width/2, data.height/2)


def mousePressed(event, data):
    if (data.rectCoords[0]<event.x<data.rectCoords[2] and 
            data.rectCoords[1]<event.y<data.rectCoords[3]):
        data.string = ""
        data.isPressed = True
    else:
        data.isPressed = False

def keyPressed(event, data):
    if data.isPressed:
        if event.keysym == "BackSpace":
            data.string = data.string[:-1]
        else:
            if event.keysym.isalnum():
                data.string = data.string + event.keysym

def timerFired(data):
    pass

def redrawAll(canvas, data):
    canvas.create_rectangle(data.rectCoords, fill = "green")
    canvas.create_text(data.textCoords, text = data.string)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 200)
