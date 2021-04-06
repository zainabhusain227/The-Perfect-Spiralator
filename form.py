import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from numpy import diff
from scipy.fft import fft, fftfreq
import math
from release_time import *
from spin_rate import *
from classes import *
from timings import *
from wrist_y_max import *
import statistics
import os
      
#read the filelist so we know which json files to import
def extract_coordinates(vid):
    data_folder = os.path.join(vid.folder_path, "allthejsons")
    filelist = os.path.join(vid.folder_path, "filelist.txt")
    #calculate number of frames
    frames = len(open(filelist).readlines(  ))
    joints=25

    #make empty array for coordinate matrix
    arr= np.zeros((joints,3,frames))
    f = open(filelist, "r")

    for i in range(frames):
        jsonfilename = os.path.join(data_folder, f.readline())
        #remove newline character from end of string
        jsonfilename = jsonfilename.rstrip("\n")
        #print(jsonfilename)

        with open(jsonfilename, 'r') as handle:
            parsed = json.load(handle)
            #print(type(parsed["people"]))
            #print(parsed["people"][15]["pose_keypoints_2d"])
            #break

        #if pose_keypoints_2d exists, then add it to the array
        try:
            coord=parsed["people"][0]["pose_keypoints_2d"]
            for j in range(joints):
                #all 3 are in the same list so needs to be seperated
                arr[j][0][i]=coord[j*3]
                arr[j][1][i]=vid.pixel_dimy - coord[(j*3)+1]
                arr[j][2][i]=coord[(j*3)+2]
                

        #write over bad frame with previous good frame
        except IndexError:
            for j in range(joints):
                #all 3 are in the same list so needs to be seperated
                arr[j][0][i]=None
                arr[j][1][i]=None
                arr[j][2][i]=None
                #print(arr[j][0][i],arr[j][1][i],arr[j][2][i])
            print("****index error*****")
    vid.frames=frames
    vid.coord_array=arr



def filtering(vid,cuttoff):
    arr=vid.coord_array
    frames=vid.frames    
    joints=25
    #remove low confidence factor frames
    for i in range(frames):
        for j in range(joints):
            #add another loop to go through all joints
            confidence=arr[j][2][i]
            if (confidence< 0.3):
                arr[j][0][i]=None
                arr[j][1][i]=None

    plt.plot(arr[2][1])
    plt.ylabel('Openpose Wrist y')
    plt.show()
    #update coordinates
    vid.coord_array=arr


def throw_phases(vid):   
    time=np.arange(vid.frames)
    a=Joint_array(vid.coord_array)
    time_3(vid)
    time_2(vid)
    time_1(vid)
    #stage 4:follow through
    #stage four follows stage 3 and occurs when the wrist is below the shoulder
    for i in range(vid.t3,vid.frames):
        if a.wrist_y[i] < a.rshoulder_y[i]:
            t4=i
            break
    vid.t4=int(t4)
    

def line_length(vid,joint1x,joint1y,joint2x,joint2y):
  length=vid.frames
  linelength_arr = np.empty(length)
  for i in range(length):
    if(joint1x[i]!=None and joint1y[i]!=None and joint2x[i]!=None and joint2y[i]!=None):
      diff_x=joint2x[i]-joint1x[i]
      diff_y=joint2y[i]-joint1y[i]
      linelength_arr[i]=np.sqrt(diff_x**2 +diff_y**2)
    #print(linelength_arr[i])
  #plt.plot(linelength_arr)
  #plt.ylabel('linelegth')
  #plt.show()
  return linelength_arr


def vector_angle(vid,elbow_x,elbow_y,rshoulder_x,rshoulder_y,neck_x,neck_y):
  #elbow, rshoulder, neck
  #returns an array of angles, length of frames
  angle_arr_len=vid.frames
  angle_arr = np.empty(angle_arr_len)
  for i in range(angle_arr_len):
    #if all entries in the array have values, otherwise leave it as null
    if(elbow_x[i]!=None and elbow_y[i]!=None and rshoulder_x[i]!=None and rshoulder_y[i]!=None and neck_x[i]!=None and neck_y[i]!=None):
      
      vector_1 = [neck_x[i]-rshoulder_x[i],neck_y[i]-rshoulder_y[i]]
      vector_2 = [elbow_x[i]-rshoulder_x[i], elbow_x[i]-rshoulder_x[i]]
      
      unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
      unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
      dot_product = np.dot(unit_vector_1, unit_vector_2)
      angle_arr[i] = np.degrees(np.arccos(dot_product))
    else:
      print("*****")
  #plt.plot(angle_arr)
  #plt.ylabel('angles')
  #plt.show()
  return angle_arr

def roc_wrist(vid,wrist_x,wrist_y):
  length=vid.frames
  roc_wrist_arr = np.empty(length-1)
  for i in range(length-1):
    #if all entries in the array have values, otherwise leave it as null
    if(wrist_x[i]!=None and wrist_y[i]!=None and wrist_x[i+1]!=None and wrist_y[i+1]!=None):
      diff_x=wrist_x[i+1]-wrist_x[i]
      diff_y=wrist_y[i+1]-wrist_y[i]
      roc_wrist_arr[i]=np.sqrt(diff_x**2 +diff_y**2)
    
  #plt.plot(roc_wrist_arr)
  #plt.ylabel('roc_wrist')
  #plt.show()
  return roc_wrist_arr
      

def wrist_hip(vid,wrist_y,lhip_y):
  length=vid.frames
  t3=vid.t3
  wrist_hip_arr = np.empty(100)
  x=0
  for i in range( t3, t3+100):
      #if all entries in the array have values, otherwise leave it as null
      if(wrist_y[i]!=None and lhip_y[i]!=None):
          wrist_hip_arr[x]= abs(wrist_y[i]-lhip_y[i])
          x=x+1
          
  wrist_hip_derivative = np.empty(x)  
  for i in range(x-1):
    #if all entries in the array have values, otherwise leave it as null
    if(wrist_hip_arr[i]!=None and wrist_hip_arr[i+1]!=None):
      wrist_hip_derivative[i]= abs(wrist_hip_arr[i+1]-wrist_hip_arr[i])

  return wrist_hip_derivative

def get_wrist_change(vid,wrist_x,wrist_y,elbow_x,elbow_y):
  length=vid.frames
  wrist_change_arr = np.empty(length)
  for i in range(length):
    if(wrist_x[i]!=None and wrist_y[i]!=None and elbow_x[i]!=None and elbow_y[i]!=None):
      diff_x=joint2x[i]-joint1x[i]
      diff_y=joint2y[i]-joint1y[i]
      linelength_arr[i]=np.sqrt(diff_x**2 +diff_y**2)
  
def form_evaluation(vid):
    time=np.arange(vid.frames)
    t1=vid.t1
    t2=vid.t2
    t3=vid.t3
    t4=vid.t4
    print(t1,t2,t3,t4)
    a=Joint_array(vid.coord_array)

    #stage 1 checklist: 180 deg Neck=1
    #0
    angles=vector_angle(vid,a.elbow_x,a.elbow_y,a.rshoulder_x,a.rshoulder_y,a.neck_x,a.neck_y)
    #check if angle is near 180 between stage 1 and stage 2 transition, take 5 points before and after t2 to see if any are close to 180
    angle=angles[t2]
    diff=abs(180-angle) #default angle difference
    #finds minimum angle difference
    for i in range(t2-5,t2+5):
      if abs(180-angles[i]) < diff:
        angle=angles[i]
        diff=abs(180-angle)
    if (diff<20):
      vid.checkpoints[0]=1
    print("Angle between upperarm and shoulder=",angle)


    #stage 2 checklist:
    #1 ,forearm and upper arm have a constant lenth btw t2 and t3
    forearm_len=line_length(vid,a.elbow_x,a.elbow_y,a.rshoulder_x,a.rshoulder_y)
    forearm_len=forearm_len[t2:t3]
    #remove empty elements in array
    forearm_len=forearm_len[np.logical_not(np.isnan(forearm_len))]

    forearm_var=statistics.variance(forearm_len)
    forearm_mean=statistics.mean(forearm_len)
    #plt.plot(forearm_len)
    #plt.ylabel('forearm_len')
    #plt.show()
    print("forearm_var=",forearm_var, " forearm_mean=",forearm_mean)
    #calculate percent error
    forearm_percent_error= 1 - (forearm_var/forearm_mean)

    upperarm_len=line_length(vid,a.elbow_x,a.elbow_y,a.wrist_x,a.wrist_y)
    upperarm_len=upperarm_len[t2:t3]
    #remove empty elements in array
    upperarm_len=upperarm_len[np.logical_not(np.isnan(upperarm_len))]
    #plt.plot(upperarm_len) 
    #plt.ylabel('upperarm_len') 
    #plt.show()
    upperarm_var=statistics.variance(upperarm_len)
    upperarm_mean=statistics.mean(upperarm_len)
    #calculate percent error
    upperarm_percent_error= 1 - (upperarm_var/upperarm_mean)
    print("upperarm_var=",upperarm_var, " upperarm_mean=",upperarm_mean)
    vid.checkpoints[1]= (forearm_percent_error*0.5) + (upperarm_percent_error*0.5)
    
    
    #stage 2 checklist: wrist max height matched 3, arm and shoulder in line
    #2
    max_wrist_time=max_wrist_y(vid) #max_wrist_y(vid)
    vid.checkpoints[2]=1 - (abs(t3-max_wrist_time)/t3)

    #stage 3 checklist:
    #3
    #roc_wrist=np.empty(vid.frames)
    rocwrist=roc_wrist(vid,a.wrist_x,a.wrist_y)
    #from 20 frames before to 20 frames after, compare the magnitudes of rate of chamge,find mean rate of change
    before_mean=statistics.mean(rocwrist[t3-20:t3])
    after_mean=statistics.mean(rocwrist[t3:t3+20])
    vid.checkpoints[4]=1- (abs(after_mean-before_mean)/before_mean)


    #stage 4 checklist:
    #5 make sure shoulders twist after throw and rshoulder_x is greater than lshoulder_x
    rshoulderx_mean=statistics.mean(a.rshoulder_x[t4:t4+20])
    lshoulderx_mean=statistics.mean(a.lshoulder_x[t4:t4+20])
    if rshoulderx_mean>lshoulderx_mean:
      vid.checkpoints[5]=1

    #6 wrist follow through y
    wrist_hip_derivative=wrist_hip(vid,a.wrist_y,a.lhip_y)
    rshoulderx_mean=statistics.mean(wrist_hip_derivative)
    #distance between wrist and hip should be decreasing till same level
    #if derivative is negative
    if rshoulderx_mean<0:
      vid.checkpoints[6]=1
    

    #7 wrist follow through x
    forearm=line_length(vid,a.wrist_x,a.wrist_y,a.elbow_x,a.elbow_y)
    x=0
    forearm_derivative=np.empty(100)
    for i in range(t3,t3+100):
        #if all entries in the array have values, otherwise leave it as null
        if(forearm[i]!=None and forearm[i+1]!=None):
            forearm_derivative[x]= abs(forearm[i+1]-forearm[i])
            x=x+1
    
    forearm_mean=statistics.mean(forearm_derivative)
    #if forearm gets smaller
    if forearm_mean<0:
      vid.checkpoints[7]=1

    print(vid.checkpoints)
    
'''
#from pathlib import Path
dir_path = os.path.dirname(os.path.realpath(__file__))
vid=Vid()
vid.folder_path= os.path.join(dir_path,"sample_video8")

extract_coordinates(vid)
#release_time(vid)

#launch_angle(vid)
#spin_rate(vid)
#krishtees spinrate

cuttoff=0.5
filtering(vid,cuttoff)
print("starting form")
throw_phases(vid)
form_evaluation(vid)
#color_overlay(vid)
spin_rate(vid)
#plot(vid)'''



