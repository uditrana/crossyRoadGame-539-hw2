# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import time

####################################
# customize these functions
####################################

raftX = 300 - 35
# (if on left, if on boat, x, y)
grain1 = (False, False, 325, 200)
grain2 = (False, False, 325, 300)
grain3 = (False, False, 325, 400)

def init(data):
    data.grainR = 10

def mousePressed(event, data):
    if (325 < event.x < 400) and (575 < event.y < 600):
        solve()

def solve():
    addGrain()
    cross()
    removeGrain()    

def removeGrain():
    global grain1, grain2, grain3
    if raftX == 100:
        if grain1[1] == True:
            grain1 = (True, False, 50, 200)
        elif grain2[1] == True:
            grain2 = (True, False, 50, 300)
        elif grain3[1] == True:
            grain3 = (True, False, 50, 400)

def addGrain():
    global raftX, grain1, grain2, grain3
    if raftX == 265:
        if grain1[0] == False:
            grain1 = (False, True, raftX + 15, 285)
        elif grain2[0] == False:
            grain2 = (False, True, raftX + 15, 285)
        elif grain3[0] == False:
            grain3 = (False, True, raftX + 15, 285)

def cross():
    global raftX
    if raftX == 265:
        raftX = 100
    else:
        raftX = 265

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    drawBackground(canvas, data)
    drawRice(canvas, data)

def drawRice(canvas, data):
    global grain1, grain2, grain3
    canvas.create_oval(grain1[2] - data.grainR, grain1[3] - data.grainR,
                       grain1[2] + data.grainR, grain1[3] + data.grainR)
    canvas.create_oval(grain2[2] - data.grainR, grain2[3] - data.grainR,
                       grain2[2] + data.grainR, grain2[3] + data.grainR)
    canvas.create_oval(grain3[2] - data.grainR, grain3[3] - data.grainR,
                       grain3[2] + data.grainR, grain3[3] + data.grainR)

def drawBackground(canvas, data):
    canvas.create_rectangle(0, 0, 400, 600, fill = "green")
    canvas.create_rectangle(100, 0, 300, 600, fill = "blue")
    canvas.create_rectangle(325, 575, 400, 600, fill = "white")
    canvas.create_text(400, 600, text = "EXECUTE", anchor = SE, font = 40)
    # raft
    canvas.create_rectangle(raftX, 270, raftX + 35,
                            300, fill = "brown")
    # person
    canvas.create_oval(raftX + 2, 260, raftX + 8, 266, fill = "black")
    canvas.create_line(raftX + 5, 266, raftX + 5, 280)
    canvas.create_line(raftX, 266, raftX + 5, 272)
    canvas.create_line(raftX + 5, 272, raftX + 10, 266)
    canvas.create_line(raftX, 286, raftX + 5, 280)
    canvas.create_line(raftX + 5, 280, raftX + 10, 286)

####################################
# use the run function as-is
####################################

def run(width, height):
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

run(400, 600)