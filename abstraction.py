distances=[10,20,30,40,50]

pathes = [(distances[0],distances[1],distances[2])],[(distances[1],distances[2],distances[3])]
path3 = [distances[4],distances[3],distances[2]]

def driveToDistance1():
    print(distances[0])

def driveToDistance2():
    print(distances[1])

def followPath1():
    print(pathes[0])

def followPath2():
    print(pathes[1])

driveToDistance1()
driveToDistance2()
followPath1()
followPath2()
