# Declare Distance + Path Values
driveDistances = {1:10, 2:20, 3:30, 4:40, 5:50}
drivePaths = {1:[10, 20, 30], 2:[20, 30, 40]}

# Define Drive + Path Functions
def driveToDistance(driveDistances):
    print(driveDistances)
def followPath(drivePaths):
    print(drivePaths)
    
# Output Distance + Path Values
driveToDistance(driveDistances[1])
driveToDistance(driveDistances[2])
followPath(drivePaths[1])
followPath(drivePaths[2])
