distance = [10, 20, 30, 40]

paths= [(distance[0], distance[1], distance[2]), (distance[1], distance[2], distance[3])]

def driveToDistance1():
    print(distance[0])

def driveToDistance2():
    print(distance[1])

def followPath1():
    print(paths[0])

def followPath2():
    print(paths[1])

driveToDistance1()
driveToDistance2()
followPath1()
followPath2()
