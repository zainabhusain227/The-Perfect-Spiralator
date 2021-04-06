import numpy as np
import cv2
from classes import *
from matplotlib import pyplot as plt
from scipy import stats


def spin_rate(vid):
    #masked_clip = os.path.join(vid.folder_path, "masked_clip.mp4")
    vidcap = cv2.VideoCapture("mask.mp4")
    success,image = vidcap.read()
    count = 0
    pixels = []
    while success:
      
      #detect purple and create a mask
      hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
      lower = np.array([125,0,0])
      upper = np.array([170,255,255])
      mask1 = cv2.inRange(hsv, lower, upper)
     

      mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
      mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))

      #count number of purple pixels
      countpix = cv2.countNonZero(mask1)
      pixels.append(countpix)


      success,image = vidcap.read()
      count += 1

    
    t3 = vid.t3
    pixels = pixels[t3:]

    #fill in empty elements
    for x in range(1,len(pixels)-1):
        if (pixels[x] == 0):
          pixels[x] = pixels[x-1]


    #smooth pixels
    sm1 = pixels[0]
    smooth = [sm1]

    for x in range(1,len(pixels)):
      new = (0.05*pixels[x]) + (0.95*smooth[x-1])
      smooth.append(new)

    sm2 = smooth[0]
    smooth2 = [sm2]
    for x in range(1,len(pixels)):
      new = (0.2*smooth[x]) + (0.8*smooth2[x-1])
      smooth2.append(new)

    #find maxes
    maximums = []
    frame = []
    for x in range(1, len(pixels)-1):
      if ((smooth[x]>smooth[x-1]) and (smooth[x]>smooth[x+1])):
        maximums.append(smooth[x])
        frame.append(x)


    #outlier elimination using iqr
    iqr = stats.iqr(maximums)
    q1 = np.percentile(maximums, 25)
    q3 = np.percentile(maximums, 75)
    lower = q1 - 1.5*iqr
    upper = q3 + 1.5*iqr
    print('iqr is', iqr, q1,q3, lower, upper)

    for x in range(len(maximums)):
      if (maximums[x]<lower or maximums[x]>upper):
        frame.pop(x)
        
    delta = []
    for x in range(len(frame)-1):
      delta.append(frame[x+1]-frame[x])

    avg = sum(delta)/(len(delta))
    rpm = 240*60/avg

    vid.spin = rpm  


