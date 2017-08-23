import random

roomX = 5
roomY = 5
userX = 1
userY = 1
doorX = 3
doorY = 5
answerDoor = "That is a door"
answerWall = "That is a wall"
answerEmpty = "You walked, good job"

def move(direction):
    global roomX
    global roomY
    global userX
    global userY
    global doorX
    global doorY
    if direction.lower() == "up":
        if userY + 1 > roomY:
            print answerWall
        else:
            userY += 1
            if userY == doorY and userX == doorX:
                print answerDoor
            else:
                print answerEmpty
    elif direction.lower() == "down":
        if userY - 1 < 1:
            print answerWall
        else:
            userY -= 1
            if userY == doorY and userX == doorX:
                print answerDoor
            else:
                print answerEmpty
    elif direction.lower() == "left":
        if userX - 1 < 1:
            print answerWall
        else:
            userX -= 1
            if userY == doorY and userX == doorX:
                print answerDoor
            else:
                print answerEmpty
    elif direction.lower() == "right":
        if userX + 1 > roomX:
            print answerWall
        else:
            userX += 1
            if userY == doorY and userX == doorX:
                print answerDoor
            else:
                print answerEmpty
    
def createRoom():
    print 0