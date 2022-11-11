distances={'distance1': 10,'distance2': 20,'distance3':30,'distance4': 40, 'distance5': 50}
paths={'path1': [distance1, distance2, distance3], 'path2': [distance2, distance3, distance4], 'path3': [distance5, distance4, distance3]}


def driveToDistances():
    print(distances)

def followPaths():
    print(paths)



driveToDistance1([distance1])
driveToDistance2([distance2])
followPath1([path1])
followPath2([path2])
