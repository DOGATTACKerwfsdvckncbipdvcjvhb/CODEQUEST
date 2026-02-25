import sys
import math

testcases = int(sys.stdin.readline().rstrip())

#wait wait wait wait
# lets make the plan first so we dont do different things
#okay lets start by taking inputs
# wait so now lets make a space ship class
# yes
class Spaceship:
    def __init__(self, name, x, y, shipclass):
        self.name = name
        self.shipclass = shipclass
        self.x = x
        self.y = y


def find_closest_ship(): 
    closestship = Spaceship(ships[0].name, ships[0].x, ships[0].y, ships[0].shipclass) 
    a = 1
    poppingIndex = 0
    while a < len(ships):
        if ships[a].x < closestship.x or (ships[a].x == closestship.x and ships[a].y > closestship.y):
            closestship.name = ships[a].name
            closestship.x = ships[a].x
            poppingIndex = a
        a += 1
    ships.pop(poppingIndex - 1) # so is it something here I think - 1 shoulf 
    return closestship
        
      

answer = ""


for i in range(testcases):
    ships = [] 
    amountOfships = int(sys.stdin.readline().rstrip())
    for b in range(amountOfships):
        line = (sys.stdin.readline().rstrip()).split(":")
        nameAndclass = line[0].split("_")
        name = nameAndclass[0]
        shipclass = nameAndclass[1] # what is the error(s)
        XandY = line[1].split(",")
        x = int(XandY[0])
        y = int(XandY[1])
        ship = Spaceship(name, x, y, shipclass)
        ships.append(ship)
    destroyedShips = ""
    
    count = 0
    while count < amountOfships:

        closestship = find_closest_ship()
        answer += f"Destroyed Ship: {closestship.name} xLoc: {closestship.x}\n"
        
        for ac in ships:
            Shipclass = ac.shipclass
            if shipclass == 'C':
                ac.x -= 30 
            elif shipclass == 'B':
                ac.x -= 20
            else:
                ac.x -= 10

        count+=1
    

print(answer.rstrip())
# acess