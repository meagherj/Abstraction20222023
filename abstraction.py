distance = {1:10, 2:20, 3:30, 4:40, 5:50}

paths = {1:[distance[1], distance[2], distance[3]], 2:[distance[2], distance[3], distance[4]]}

driveToDistance = [(distance[1]), (distance[2])]

followPath = [(paths[1]), (paths[2])]

def driveToDistance(d):
    print(distance[d])
def followPath(f):
    print(paths[f])

driveToDistance(1)
driveToDistance(2)
followPath(1)
followPath(2)
