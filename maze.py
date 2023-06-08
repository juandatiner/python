import readchar
import os

POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

myPosition = [4, 3]

while True:
    #Draw map
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end = "")
        for coordinate_x in range(MAP_WIDTH):
            
            #Draw initial position
            if myPosition[POS_X] == coordinate_x and myPosition[POS_Y] == coordinate_y:
                print(" @ ", end = "")
            else:
                print("   ", end = "")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")   

    #Move from position
    direction = readchar.readchar()

    if direction == "w":
        myPosition[POS_Y] -= 1
    elif direction == "s":
        myPosition[POS_Y] += 1
    elif direction == "a":
        myPosition[POS_X] -= 1 
    elif direction == "d":
        myPosition[POS_X] += 1
    elif direction == "q":
        break
    
    os.system("cls")
