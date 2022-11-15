
distance = {1: 10, 2:20, 3:30, 4: 40}

# dictionary (above)

path = {1 : [distance[1],distance[2],distance[3]], 2 : [distance[2],distance[3],distance[4]]}


def driveToDist(x):
    print(distance[x])

def followPath(x):
    print(path[x])

driveToDist(1)
driveToDist(2)
driveToDist(3)
followPath(1)
followPath(2)

