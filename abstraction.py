
distanceList = [10,20,30,40,50]

paths = {
    "path1":[distanceList[0],distanceList[1],distanceList[2]],
    "path2":[distanceList[1],distanceList[2],distanceList[3]],
    "path3":[distanceList[4],distanceList[3],distanceList[2]]
    }

def driveToDistance(distance1):
    print(distance1)

driveToDistance(distanceList[0])
driveToDistance(distanceList[1])
driveToDistance(paths["path1"])
driveToDistance(paths["path2"])
