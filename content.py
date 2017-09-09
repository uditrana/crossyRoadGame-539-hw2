# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################

raftX = 300 - 35

def init(data):
    data.riceR = 10
    data.riceX1, data.riceY1 = 325, 200
    data.riceX2, data.riceY2 = 325, 300
    data.riceX3, data.riceY3 = 325, 400

def mousePressed(event, data):
    if (325 < event.x < 400) and (550 < event.y < 600):
        solve()

def solve():
    cross()

def cross():
    global raftX
    raftX = 100

def keyPressed(event, data):
    pass

def timerFired(data):
    print(raftX)

def redrawAll(canvas, data):
    drawBackground(canvas, data)

def drawBackground(canvas, data):
    canvas.create_rectangle(0, 0, 400, 600, fill = "green")
    canvas.create_rectangle(100, 0, 300, 600, fill = "blue")
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
    # rice
    canvas.create_oval(data.riceX1 - data.riceR, data.riceY1 - data.riceR,
                       data.riceX1 + data.riceR, data.riceY1 + data.riceR)
    canvas.create_oval(data.riceX2 - data.riceR, data.riceY2 - data.riceR,
                       data.riceX2 + data.riceR, data.riceY2 + data.riceR)
    canvas.create_oval(data.riceX3 - data.riceR, data.riceY3 - data.riceR,
                       data.riceX3 + data.riceR, data.riceY3 + data.riceR)

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