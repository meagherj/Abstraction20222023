
distances = {1:10, 2:20, 3:30, 4:40, 5:50}

path = {1:[10, 20, 30], 2:[20, 30, 40]}

def driveToDistance(distance):
    print(distance)

def followPath(path):
    print(path)

driveToDistance(distances[1])
driveToDistance(distances[2])
followPath(path[1])
followPath(path[2])
