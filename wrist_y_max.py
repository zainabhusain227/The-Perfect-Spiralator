import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from numpy import diff
import os
import math
import operator
import statistics
from classes import *

def max_wrist_y(vid):
  a = Joint_array(vid.coord_array)
  wrist_y = a.wrist_y
  

  max_loc = []

  wrist_sorted = sorted(wrist_y, reverse = True)
  maxes = wrist_sorted[:10]

  wrist_y = list(wrist_y)
  for x in range(9):
    max_indx = wrist_y.index(maxes[x])  
    max_loc.append(max_indx)

  max_loc = list(max_loc)
  #print(max_loc)
  max2 = statistics.median(max_loc)

  #print('wrist max is', maxi, max1, max2, max3)

  wrist_y_max = max2
  return wrist_y_max
