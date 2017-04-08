# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import spotipy
import sys
import pprint
sp = spotipy.Spotify()
####################################
# customize these functions
####################################

# class Input(object):
#     def __init__

def init(data):
    data.string = "Search for Songs Here!"
    data.isPressed = None
    data.rectCoords = (data.width/2-100, 20,data.width/2+100,60)
    data.textCoords = (data.width/2, 40)
    #data.cursorCoords = (data.width/2, data.height/2)
    data.cursorOn = False
    data.timerCount = 0
    data.search = ""


def mousePressed(event, data):
    if (data.rectCoords[0]<event.x<data.rectCoords[2] and 
            data.rectCoords[1]<event.y<data.rectCoords[3]):
        if data.isPressed is None:
            data.string = ""
        data.isPressed = True
    else:
        data.isPressed = False

def keyPressed(event, data):
    if data.isPressed:
        if event.keysym == "BackSpace":
            if len(data.string) > 0:
                if data.string[-1] == "|":
                    data.string = data.string[:-2]
                else:
                    data.string = data.string[:-1]
        elif event.keysym == "space":
            if len(data.string) > 0 and data.string[-1] == "|":
                data.string = data.string[:-1] + " "
            else:
                data.string = data.string + " "
        elif event.keysym == "Return":
            data.isPressed = False
            data.search = data.string
            data.songs = search(data)
        else:
            if len(event.keysym)==1:
                if len(data.string) > 0 and data.string[-1] == "|":
                    data.string = data.string[:-1] + event.keysym
                else:
                    data.string = data.string + event.keysym

def timerFired(data):
    data.timerCount+=1
    if data.timerCount%5 == 0:
        if data.isPressed:
            if data.cursorOn:
                data.cursorOn = False
                if "|" in data.string:
                    index = data.string.index("|")
                    data.string = data.string[:index] + data.string[index+1:]
            else:
                data.cursorOn = True
                data.string += "|"
    
def drawSongs(canvas, data):
    for i in range(len(data.songs)):
        song, artist = data.songs[i]
        drawIndivSong(canvas, i, song, artist)

def drawIndivSong(canvas, num, song, artist):
    canvas.create_text(20, 100 + 60*num, text = song + " -- " + artist, 
            anchor = "w")

def search(data):
    if data.search[-1] == '|':
        data.search = data.search[:-1]
    result = sp.search(data.search)
    result = result['tracks']['items']
    songList = []
    for res in result:
        if res['type'] == 'track':
            songTitle = res['name']
            artist = res['artists'][0]['name']
            songList.append((songTitle, artist))
    return songList


def redrawAll(canvas, data):
    canvas.create_rectangle(data.rectCoords, fill = "green")
    canvas.create_text(data.textCoords, text = data.string)
    if data.search != "":
        drawSongs(canvas, data)

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

run(800, 600)
