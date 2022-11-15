# Declare Distance + Path Values
driveDistances = {1:10, 2:20, 3:30, 4:40, 5:50}
drivePaths = {1:[10, 20, 30], 2:[20, 30, 40]}

# Define Drive + Path Functions
def driveToDistance(distance):
    print(distance)
def followPath(path):
    print(path)
    
# Output Distance + Path Values
driveToDistance(distances[1])
driveToDistance(distances[2])
followPath(path[1])
followPath(path[2])
