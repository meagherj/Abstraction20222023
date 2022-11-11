
distance10 = 10
distance20 = 20
distance30 = 30
distance40 = 40
distance50 = 50

path1 = [distance10,distance20,distance30]
path2 = [distance20,distance30,distance40]
path3 = [distance50,distance40,distance30]

def driveFor10():
    print(distance10)

def driveFor20():
    print(distance20)

def followPath1():
    print(path1)

def followPath2():
    print(path2)

driveToDistance1()
driveToDistance2()
followPath1()
followPath2()
