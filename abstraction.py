distances={'distance1': 10,'distance2': 20,'distance3':30,'distance4': 40, 'distance5': 50}
paths={'path1': [distances ['distance1'] , distances ['distance2'] , distances ['distance2']], 'path2': [distances ['distance2'], distances ['distance3'], distances ['distance4']], 'path3': [distances ['distance5'], distances['distance4'], distances['distance3']}


def driveToDistances(distance):
    print(distance)
 

def followPaths(path):
    print(path)



driveToDistances(distances['distance1'])
driveToDistances(distances['distance2'])
followPaths(paths['path1'])
followPaths(paths['path2'])
