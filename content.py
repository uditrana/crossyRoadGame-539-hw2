# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import time

####################################
# customize these functions
####################################


class Raft(object):
    def __init__(self):
        self.position = False
        self.inRaft = None
        self.x = 290  # center coordinates
        self.y = 270
        self.width = 35
        self.height = 30

    def cross(self):
        self.position = not self.position
        self.x = 110
        if self.inRaft != None:
            self.inRaft.x = self.x
            self.inRaft.y = self.y

    def draw(self, canvas):
        canvas.create_rectangle(self.x - self.width / 2, self.y - self.height / 2,
                                self.x + self.width / 2, self.y + self.height / 2, fill="brown")

    def boardRaft(self, obj):
        self.inRaft = obj
        obj.getInRaft(self)

    def deboardRaft(self):
        self.inRaft.getOffRaft(raft)
        self.inRaft = None


class Passenger(object):
    def __init__(self, ycord):
        self.position = False  # true=left, None = inRaft, false = right
        self.leftX = 75
        self.rightX = 325
        self.x = self.rightX  # current spot
        self.restingY = ycord  # y cord for while not in boat
        self.y = ycord

    def getInRaft(self, raft):
        self.position = None
        self.x = raft.x
        self.y = raft.y

    def getOffRaft(self, raft):
        self.position = raft.position
        self.y = self.restingY
        if self.position == False:
            self.x = self.rightX
        else:
            self.x = self.leftX


class Grain(Passenger):
    def __init__(self, ycord):
        super().__init__(ycord)
        self.r = 10

    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r,
                           self.x + self.r, self.y + self.r)


raft = Raft()
grain1 = Grain(200)
grain2 = Grain(300)
grain3 = Grain(400)
grainList = [grain1, grain2, grain3]


def init(data):
    pass


def mousePressed(event, data):
    if (325 < event.x < 400) and (575 < event.y < 600):
        studentInput()


def studentInput():
    addGrain()
    cross()
    removeGrain()
    cross()
    addGrain()
    cross()
    removeGrain()
    cross()
    addGrain()
    cross()
    removeGrain()


def removeGrain():
    global raft, grainList
    if raft.inRaft == None:
        print("Raft already empty!")
        return
    raft.deboardRaft()


def addGrain():
    global raft, grainList
    if raft.inRaft != None:
        print("Raft already has something in it!")
        return
    for grain in grainList:
        if grain.position == raft.position:
            raft.boardRaft(grain)
            break


def cross():
    global raft, grainList
    raft.cross()


def keyPressed(event, data):
    pass


def timerFired(data):
    pass


def redrawAll(canvas, data):
    drawBackground(canvas, data)


def drawBackground(canvas, data):
    global raft, grainList
    canvas.create_rectangle(0, 0, 400, 600, fill="green")
    canvas.create_rectangle(100, 0, 300, 600, fill="blue")
    canvas.create_rectangle(325, 575, 400, 600, fill="white")
    canvas.create_text(400, 600, text="EXECUTE", anchor=SE, font=40)
    # raft
    raft.draw(canvas)
    # rice
    for grain in grainList:
        grain.draw(canvas)

    # person
    # canvas.create_oval(raftX + 2, 260, raftX + 8, 266, fill = "black")
    # canvas.create_line(raftX + 5, 266, raftX + 5, 280)
    # canvas.create_line(raftX, 266, raftX + 5, 272)
    # canvas.create_line(raftX + 5, 272, raftX + 10, 266)
    # canvas.create_line(raftX, 286, raftX + 5, 280)
    # canvas.create_line(raftX + 5, 280, raftX + 10, 286)

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

    class Struct(object):
        pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100  # milliseconds
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
