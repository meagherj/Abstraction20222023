dis_dict = {'distance1':10,'distance2':20,'distance3':30,'distance4':40,'distance5':50,}
            
path_dict = {'path1':[dis_dict['distance1'] , dis_dict['distance2'] , dis_dict['distance3']] , 'path2':[dis_dict['distance2'] , dis_dict['distance3'] , dis_dict['distance4']] , 'path3':[dis_dict['distance5'] , dis_dict['distance4'] , dis_dict['distance3']]}
      
def driveToDistance(dis_dict):
    print(dis_dict)
            
def followPath(path_dict):
    print(path_dict)


driveToDistance(dis_dict['distance1'])
driveToDistance(dis_dict['distance2'])

followPath(path_dict['path1'])
followPath(path_dict['path2'])
