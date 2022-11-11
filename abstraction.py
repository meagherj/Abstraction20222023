distances= {1:10, 2:20, 3:30, 4:40, 5:50}

paths= {1:[distances[1],distances[2],distances[3]], 2:[distances[2],distances[3],distances[4]], 3:[distances[5],distances[4],distances[3]]}

def driveToDistance(Distance):
    print(Distance)

def followPath(Path):
    print(Path)

driveToDistance(distances[1])
driveToDistance(distances[2])
followPath(paths[1])
followPath(paths[2])
