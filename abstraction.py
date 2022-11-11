distances = [10,20,30,40]
index = { 'path1' : [distances[0], distances[1], distances[2]],
'path2' : [distances[1], distances[2], distances[3]]}

def driveToDistancesandfollowPaths(d1,d2):
    print (distances[d1],distances[d2])
    print (index['path1'],index['path2'])

driveToDistancesandfollowPaths(0,1)
