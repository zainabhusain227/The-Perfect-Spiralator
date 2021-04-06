import numpy as np

class Vid:
  def __init__(vid):
    #create video class to be passed btw functions
    vid.folder_path=""
    vid.coord_array=0
    vid.pixel_dimx=1080
    vid.pixel_dimy=1920
    vid.frames=0
    vid.framerate=1
    vid.t4=0
    vid.t3=0
    vid.t2=0
    vid.t1=0
    vid.tragectory=0
    vid.Spinrate=0
    vid.checkpoints=np.zeros(8)


class Joint_array:
  def __init__(joint_array,arr):
    #create video class to be passed btw functions
    joint_array.neck_x=arr[1][0]
    joint_array.rshoulder_x=arr[2][0]
    joint_array.lshoulder_x=arr[5][0]
    joint_array.elbow_x=arr[3][0]
    joint_array.wrist_x=arr[4][0]
    
    #y axis
    joint_array.neck_y=arr[1][1]
    joint_array.rshoulder_y=arr[2][1]
    joint_array.elbow_y=arr[3][1]
    joint_array.wrist_y=arr[4][1]
    joint_array.lhip_y=arr[12][1]
   
    #confidence factor
    joint_array.neck_c=arr[1][2]
    joint_array.rshoulder_c=arr[2][2]
    joint_array.elbow_c=arr[3][2]
    joint_array.wrist_c=arr[4][2]
    joint_array.lhip_c=arr[12][2]

    
