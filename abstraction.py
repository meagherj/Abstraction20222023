import os
os.system('cls')

distances = [10,20,30,40]

allpaths = {1:[distances[0], distances[1], distances[2]], 2:[distances[1], distances[2], distances[3]]}

def driveToDistances(distance):
    print(distance)
    
def followPath1(mypath):
    print(mypath)

driveToDistances(distances[1])
driveToDistances(distances[2])
followPath1(allpaths[1])
followPath1(allpaths[2])
