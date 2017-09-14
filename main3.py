# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

####################################
# customize these functions
####################################


class Raft(object):
    def __init__(self):
        self.position = False  # true is left, False is right
        self.inRaft = None
        self.leftX = 110
        self.rightX = 290
        self.x = self.rightX  # center coordinates
        self.y = 270
        self.width = 35
        self.height = 30

    def cross(self):
        self.position = not self.position
        if self.position:
            self.x = self.leftX
        else:
            self.x = self.rightX
        if self.inRaft != None:
            self.inRaft.shore = not (self.inRaft.shore)
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


class Passenger(object):  # any passenger. Inherit from this for grain/wolf/chicken
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
        self.shore = False

    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r,
                           self.x + self.r, self.y + self.r,
                           fill = 'yellow')

class Wolf(Passenger):
    def __init__(self, ycord):
        super().__init__(ycord)
        self.r = 10
        self.shore = False

    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r,
                           self.x + self.r, self.y + self.r,
                           fill = 'grey')
class Chicken(Passenger):
    def __init__(self, ycord):
        super().__init__(ycord)
        self.r = 10
        self.shore = False

    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r,
                           self.x + self.r, self.y + self.r,
                           fill = 'red')


# global Variables (bleh)
isFull = False
grainOnBoard = False
chickenOnBoard = False
wolfOnBoard = False
running = False
raft = Raft()
grainList = [] 
for i in range(30):
    grainList.append(Grain(50+ i*15 ))


def init(data):
    pass

def pause():
    programPause = input("Press the <ENTER> key to execute next command...")

## This function is for the execute button on UI
def mousePressed(event, data):
    global running
    if (running):
        pass
    else:
        running = True
        if (325 < event.x < 400) and (575 < event.y < 600):
            studentInput()

def grainOnLeft():
    global grain
    return grain.shore   

def grainOnRight():
    return not grainOnLeft();


def didIWin():
    #this function will be rewritten in exercise 2B
    if (wolfOnLeft() and chickenOnLeft() and grainOnLeft()):
        return True
    else:
        return False

def finish():
    print ("Done!")

## for each of the exercises the student will type solution in this function
## Solutions can be found in exercises.py
def moveGrain():
    addGrain()
    cross()
    removeGrain()

def studentInput():

    # 2A - demo broken function
    # conditionalRemoveWolf() # <---- this should present a message for failure
    # conditionalAddGrain()
    # conditionalAddGrain() # <---- this should present a message for failure
    
    # 2+ (solving the puzzle)

    for trip in range(30):
        moveGrain()
        cross()
    finish()


def removeGrain():
    pause()
    global raft, isFull
    if raft.inRaft == None:
        return
    raft.deboardRaft()
    isFull = False
    grainOnBoard = False


def addGrain():
    pause()
    global raft, isFull, grainList
    # Remove condition for student to implement in 2A
    if raft.inRaft != None:
        return
    for grain in grainList:
        if grain.position == raft.position:
            raft.boardRaft(grain)
            isFull = True
            break


def isValid():
    return True

def notThere():
    global raft
    return (raft.x > raft.leftX-10 and raft.x < raft.rightX+10);

def step():
    global raft
    if (raft.position):
        raft.x = raft.x +10
    else :
        raft.x = raft.x -10
    if raft.inRaft != None:
        raft.inRaft.x = raft.x

def animatedCross():
    while(notThere()):
        step()
        pause()

def cross():
    pause()
    global raft
    animatedCross() #<--- to be implemented in task 3B
    raft.cross()
    if not(isValid()):
        print("That was not a valid cross, Game is over!")


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
    canvas.create_text(400, 600, text="START", anchor=SE, font=40)
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
    data.timerDelay = 200  # milliseconds
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
