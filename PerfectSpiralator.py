import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from numpy import diff
from scipy.fft import fft, fftfreq
import math
from form import *
from release_time import *
from spin_rate import *
from classes import *
from timings import *
from wrist_y_max import *
import statistics
import os



#from pathlib import Path
dir_path = os.path.dirname(os.path.realpath(__file__))
vid=Vid()
vid.folder_path= os.path.join(dir_path,"output")

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
#plot(vid)
    
