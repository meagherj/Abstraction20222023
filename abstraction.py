lst = [10, 20, 30, 40, 50]

paths = {'path1':[10, 20, 30], 'path2':[20, 30, 40], 'path3':[50, 40, 30]}

def driveDistance(dist):
    print(dist)

def followPath(pathlst):
    print(pathlst[0],pathlst[1],pathlst[2])

driveDistance(lst[0])

driveDistance(lst[1])

followPath(paths['path1'])

followPath(paths['path2'])

followPath(paths['path3'])
