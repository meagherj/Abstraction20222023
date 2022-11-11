d = {1:10, 2:20, 3:30, 4:40, 5:50}
path = {1:[d[1], d[2], d[3]], 2:[d[2], d[3], d[4]], 3:[d[5], d[4], d[3]]}

def driveToDistance(a):
    print(d[a])

def followPath(b):
    print(path[b])

driveToDistance(1)
driveToDistance(2)
followPath(1)
followPath(2)
