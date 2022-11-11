
distances=[10,20,30,40,50]

path1 = [distances[0],distances[1],distances[2]]
path2 = [distances[1],distances[2],distances[3]]
path3 = [distances[4],distances[3],distances[2]]

def driveToDistance1():
    print(distances[0])

def driveToDistance2():
    print(distances[1])

def followPath1():
    print(path1)

def followPath2():
    print(path2)

driveToDistance1()
driveToDistance2()
followPath1()
followPath2()
