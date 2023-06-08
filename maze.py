
POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

myPosition = [4, 3]

#Dibujar mapa
print(" ")
print("+" + "-" * MAP_WIDTH * 3 + "+")

for coordinate_y in range(MAP_HEIGHT):
    print("|", end = "")
    for coordinate_x in range(MAP_WIDTH):
        if myPosition[POS_X] == coordinate_x and myPosition[POS_Y] == coordinate_y:
            print(" @ ", end = "")
        else:
            print("   ", end = "")
    print("|")

print("+" + "-" * MAP_WIDTH * 3 + "+")   


