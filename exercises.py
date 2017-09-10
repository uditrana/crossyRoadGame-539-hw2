'''
solutions.py

##############################################

hw2: CS1 Content Game

##############################################

Collaborators:
Eugene Luo: eyluo
Omar Shafie: oshafie
Udit Ranasaria: uar
Preston Vander Vos: pvanderv

##############################################
This CS1 content game, Inspired from the crossing riddle: https://youtu.be/ADR7dUoVh_c , 
we decided to make the Wolf, Chicken, and Grain riddle. The object is to ferry each of these 
animals/items across a river from the right to the left side without isolating either the chicken/grain or the 
wolf/chicken. For each section, we have the student build up a part of the riddle until they have the final riddle 
solved.

##############################################

Part 1: Functions
This exercise has the student get accustomed to function calls. We begin with a farmer with three bags of grain
trying to cross a river. The only restriction is that the farmer can only ferry one item across at a time.

##############################################

1A: Using the cross() function, which literally just moves the farmer across to the other side of the river.

Solution:

cross()

##############################################

1B: Learning to add and remove items with the add() and remove() functions. 

Solution:

remove()
cross()
addGrain()
cross()
remove()

##############################################

1C: Implementing what we learned to solve the problem. Helper function is introduced.

Solution:

def moveGrain():
    addGrain()
    cross()
    remove()

def solve():
    moveGrain()
    cross()
    moveGrain()
    cross()
    moveGrain()
    finish()

##############################################

Part 2: Conditionals
This exercise introduces the concept of limitations by changing the objects to a wolf, a chicken, and a bag of 
grain. The student is now told the conditions to solve the riddle, and will be walked through step by step to
implement their own solution.

##############################################

2A: Introduction of an isFull bool. Imagine that the farmer can't tell if an item is on his boat. Use the bool
to check.

Solution:

def conditionalAdd():
    if(not isFull):
        addGrain()

##############################################

2B: This exercise checks to see if the game is won. The student needs to write a bool to check the win condition.
This is the introduction of the "and" operator.

Solution:

def finish():
    if (wolfOnLeft and chickenOnLeft and grainOnLeft):
        return True
    else:
        return False

##############################################

2C: Now the student has to write a condition to check if a move is valid. This is where the "or" operator is
introduced, and the student needs to be able to use both to check.

Solution:

def isValid():
    if (wolfOnRight and chickenOnRight) or (chickenOnRight and grainOnRight) or (wolfOnLeft and chickenOnLeft) 
    or (chickenOnLeft and grainOnLeft):
        return False
    else:
        return True

##############################################

Part 3: Loops
These exercises introduce the concept of loops in simplifying code.

##############################################

3A: This exercise calls back to 1C. Instead of three bags of grain, there are now thirty, and the student is
encouraged to move the bags across the river.

Solution:

for trip in range(30):
    moveGrain()
    cross()

##############################################

3B: This exercise implements animation. So far, the boat has jumped from shore to shore. In this situation, 
you now step one at a time until you hit the shore.

Solution:

def cross():
    while(notThere):
        step()

##############################################

3C: This exercise introduces nested loops and combines the two previous exercises. The student now needs to 
move the thirty bags of grain and step, both with loops.

Solution:

for trip in range(30):
    addGrain()
    while(notThere):
        step()
    remove()
    while(notThere):
        step()

##############################################
'''