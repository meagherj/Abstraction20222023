
distances = [10, 20, 30, 40, 50]


paths = {"path1" : [distances[0], distances[1], distances[2]],
         "path2" : [distances[1], distances[2], distances[3]],
         "path3" : [distances[4], distances[3], distances[2]]  }


def driveToDistance(distance):
    print(distance)


def followPath(path):
    print(path)


driveToDistance(distances[0])
driveToDistance(distances[1])
followPath(paths["path1"])
followPath(paths["path2"])
