distance1 = 10
distance2 = 20
distance3 = 30
distance4 = 40
distance5 = 50
path1 =''
path2 =''
path3=''

paths = {path1: [distance1,distance2,distance3], path2 : [distance2,distance3,distance4],
        path3 : [distance5,distance4,distance3]}


def driveToDistances():
    print(distance1)
    print(distance2)

def followPaths():
    print(path1)
    print(path2)

driveToDistances()
followPaths()
