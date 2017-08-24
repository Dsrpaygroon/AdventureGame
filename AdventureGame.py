import random

# [[roomX, roomY], [UserX, UserY], [[Door1X, Door1Y], [Door2X, Door2Y], etc.]
roomValues = [[5,5],[1,1],[3,5]]
answerDoor = "There is a portal in front of you"
answerWall = "That is a wall"
answerEmpty = "You walked, good job"
answerOrb = "There is a large orb at your feet"
answerPickUp = "You picked up the large orb"
answerNothing = "There is nothing to pick up"

def move(direction, roomValues):
    if direction.lower() == "up":
        if roomValues[1][1] + 1 > roomValues[0][1]:
            print answerWall
        else:
            roomValues[1][1] += 1
            if roomValues[1][1] == roomValues[2][1] and roomValues[1][0] == roomValues[2][0]:
                print answerDoor
            else:
                if roomValues[1][0] == roomValues[3][0] and roomValues[1][1] == roomValues[3][1]:
                    print answerOrb
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
                if roomValues[1][0] == roomValues[3][0] and roomValues[1][1] == roomValues[3][1]:
                    print answerOrb
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
                if roomValues[1][0] == roomValues[3][0] and roomValues[1][1] == roomValues[3][1]:
                    print answerOrb
                else:        
                    print answerEmpty
    elif direction.lower() == "right":
        if roomValues[1][0] + 1 > roomValues[0][0]:
            print answerWall
        else:
            roomValues[1][0] += 1
            if roomValues[1][1] == roomValues[2][1] and roomValues[1][0] == roomValues[2][0]:
                print answerDoor
            else:
                if roomValues[1][0] == roomValues[3][0] and roomValues[1][1] == roomValues[3][1]:
                    print answerOrb
                else:        
                    print answerEmpty
                
def useDoor(roomValues):
    print "You walk through the portal into a new room."
    roomValues = createRoom(roomValues)
    
def createRoom(roomValues):
    roomValues[0][0] = random.randint(3,10)
    roomValues[0][1] = random.randint(3,10)
    roomValues[3][0] = random.randint(2, roomValues[0][0])
    roomValues[3][1] = random.randint(2, roomValues[0][1])
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
        
def pickUp(roomValues):
    if roomValues[1][0] == roomValues[3][0] and roomValues[1][1] == roomValues[3][1]:
        print answerPickUp
        return 1
        
    else:
        print answerNothing

def play():
    roomValues = [[5,5],[1,1],[3,5],[3,3]]
    key = 0
    print "Welcome to the game, enter a direction to start your journey, and enter 'Done' when you are finished"
    print "Enter HELP for assistance"
    action = raw_input("Action: ")
    while action.lower() != "done":
        move(action, roomValues)
        if action.lower() == "open":
            if key == 1:
                useDoor(roomValues)
            else:
                print "The portal doesn't do anything"
        elif action.lower() == "pick up":
            key = pickUp(roomValues)
        action = raw_input("Action: ")
    print "Thank you for playing!"
