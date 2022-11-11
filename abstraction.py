distances = {1:10,2:20,3:30,4:40}

paths = {1:[distances[1],distances[2],distances[3]],2:[distances[2],distances[3],distances[4]]}

def driveForDistance(distance):
    print(distance)

def followPath(path):
    print(path)

driveForDistance(distances[1])
driveForDistance(distances[2])
followPath(paths[1])
followPath(paths[2])
