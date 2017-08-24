import random

# [[roomX, roomY], [UserX, UserY], [[Door1X, Door1Y], [Door2X, Door2Y], etc.]
roomValues = [[5,5],[1,1],[3,5]]
answerDoor = "That is a door"
answerWall = "That is a wall"
answerEmpty = "You walked, good job"

def move(direction):
    global roomValues
    if direction.lower() == "up":
        if roomValues[1][1] + 1 > roomValues[0][1]:
            print answerWall
        else:
            roomValues[1][1] += 1
            if roomValues[1][1] == roomValues[2][1] and roomValues[1][0] == roomValues[2][0]:
                print answerDoor
            else:
                print answerEmpty
    elif direction.lower() == "down":
        if roomValues[1][1] - 1 < 1:
            print answerWall
        else:
            roomValues[1][1] -= 1
            if roomValues[1][1] == roomValues[2][1] and roomValues[1][0] == roomValues[2][0]:
                print answerDoor
            else:
                print answerEmpty
    elif direction.lower() == "left":
        if roomValues[1][0] - 1 < 1:
            print answerWall
        else:
            roomValues[1][0] -= 1
            if roomValues[1][1] == roomValues[2][1] and roomValues[1][0] == roomValues[2][0]:
                print answerDoor
            else:
                print answerEmpty
    elif direction.lower() == "right":
        if roomValues[1][0] + 1 > roomValues[2][0]:
            print answerWall
        else:
            roomValues[1][0] += 1
            if roomValues[1][1] == roomValues[2][1] and roomValues[1][0] == roomValues[2][0]:
                print answerDoor
            else:
                print answerEmpty
                
def useDoor():
    global roomValues
    print "You walk through the doorway into a new room."
    roomValues = createRoom(roomValues)
    
def createRoom(roomValues):
    roomValues[0][0] = random.randint(3,10)
    roomValues[0][1] = random.randint(3,10)
    door = random.randint(1,4)
    
    if roomValues[1][1] == roomValues[2][1] and roomValues[1][1] == roomValues[0][1]:
        #If door was on the top
        roomValues[1][1] = 1
    elif roomValues[1][0] == roomValues[2][0] and roomValues[1][0] == roomValues[0][1]:
        #If door was on the right
        roomValues[1][0] = 1
    elif roomValues[1][1] == 1 and roomValues[2][1] == 1:
        #If door was on the bottem
        roomValues[1][1] = roomValues[0][1]
    else:
        #If door was on the left
        roomValues[1][0] = roomValues[0][0]
            
    if door == 1:
        #If door is on the top
        roomValues[2][0] = random.randint(1, roomValues[0][0])
        roomValues[2][1] = roomValues[0][1]
    elif door == 2:
        #If door is on the right
        roomValues[2][0] = roomValues[0][0]
        roomValues[2][1] = random.randint(1, roomValues[0][1])
    elif door == 3:
        #If door is on the bottem
        roomValues[2][0] = random.randint(1, roomValues[0][0])
        roomValues[2][1] = 1
    else:
        #If door is on the left
        roomValues[2][0] = 1
        roomValues[2][1] = random.randint(1, roomValues[0][1])
