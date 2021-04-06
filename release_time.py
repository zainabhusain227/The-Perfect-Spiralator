from classes import *
import numpy as np
import matplotlib.pyplot as plt
import math
import statistics 
def release_time(vid):
    ball = [None, (330, 756, 98, 70, '68%'), (331, 759, 97, 66, '65%'), (333, 761, 95, 63, '31%'), None, None, None, None, None, None, None, (334, 762, 91, 62, '44%'), (335, 762, 90, 61, '55%'), (336, 763, 89, 60, '45%'), (337, 764, 87, 59, '35%'), None, None, None, None, None, None, None, None, (335, 760, 90, 59, '30%'), (336, 761, 89, 58, '26%'), None, (336, 759, 89, 61, '35%'), (337, 759, 86, 61, '27%'), (337, 758, 87, 63, '47%'), (337, 758, 88, 62, '69%'), (335, 759, 90, 61, '71%'), (335, 758, 91, 62, '68%'), (335, 759, 92, 61, '48%'), (336, 759, 90, 60, '38%'), None, None, (336, 759, 92, 59, '25%'), (336, 756, 93, 55, '32%'), (335, 754, 94, 58, '58%'), (335, 755, 95, 57, '57%'), (334, 754, 96, 58, '62%'), (336, 754, 94, 60, '80%'), (339, 753, 90, 60, '82%'), (343, 755, 87, 56, '77%'), (343, 756, 86, 54, '78%'), (344, 755, 86, 55, '76%'), (344, 755, 87, 54, '75%'), (344, 752, 86, 56, '76%'), (343, 751, 88, 59, '87%'), (342, 750, 90, 60, '89%'), (343, 750, 88, 59, '86%'), (342, 749, 88, 60, '89%'), (343, 749, 87, 59, '86%'), (347, 750, 83, 56, '82%'), (348, 750, 83, 55, '86%'), (345, 750, 89, 55, '86%'), (345, 750, 87, 54, '38%'), (346, 749, 87, 55, '64%'), None, None, None, None, (347, 749, 87, 51, '34%'), (347, 745, 93, 56, '93%'), (348, 745, 91, 54, '88%'), (347, 748, 90, 48, '76%'), (347, 748, 91, 46, '33%'), (346, 744, 93, 51, '58%'), (358, 740, 80, 52, '61%'), (363, 741, 72, 47, '40%'), (363, 738, 72, 47, '79%'), None, None, (356, 732, 82, 52, '49%'), None, (361, 731, 74, 50, '35%'), (365, 726, 71, 58, '32%'), (361, 726, 76, 52, '56%'), None, None, None, None, None, (358, 705, 84, 54, '31%'), None, None, None, None, (365, 687, 83, 60, '70%'), (362, 684, 85, 63, '93%'), (364, 683, 82, 65, '94%'), (365, 681, 81, 68, '93%'), (365, 680, 80, 65, '92%'), (366, 679, 77, 68, '88%'), (360, 680, 75, 64, '31%'), (363, 674, 77, 62, '51%'), (357, 672, 86, 61, '60%'), (358, 672, 83, 60, '63%'), (354, 667, 90, 64, '79%'), (356, 666, 89, 66, '69%'), (359, 665, 85, 64, '55%'), (365, 667, 82, 58, '27%'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, (380, 633, 50, 66, '29%'), None, (379, 633, 52, 66, '44%'), (382, 632, 47, 67, '71%'), (381, 632, 48, 67, '46%'), (378, 630, 52, 69, '85%'), (377, 631, 52, 66, '79%'), (378, 633, 50, 64, '60%'), (378, 632, 51, 66, '65%'), (380, 631, 48, 66, '58%'), (380, 631, 47, 64, '40%'), (381, 632, 44, 62, '47%'), (380, 631, 44, 64, '57%'), (381, 631, 45, 64, '51%'), (379, 629, 47, 66, '39%'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, (384, 666, 65, 64, '28%'), (382, 666, 73, 62, '66%'), (383, 667, 68, 63, '53%'), None, (386, 668, 65, 62, '27%'), (385, 667, 66, 64, '34%'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, (332, 709, 57, 61, '53%'), (331, 709, 56, 62, '44%'), (331, 707, 55, 62, '86%'), None, None, None, None, None, None, None, (319, 707, 57, 56, '43%'), (319, 707, 58, 57, '27%'), (318, 703, 57, 60, '38%'), (317, 704, 59, 59, '26%'), None, (310, 699, 50, 74, '29%'), (311, 695, 47, 79, '25%'), None, (320, 687, 54, 73, '41%'), (296, 691, 69, 83, '36%'), (321, 684, 49, 73, '27%'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, (67, 555, 95, 87, '63%'), (68, 554, 98, 83, '59%'), (66, 552, 96, 92, '94%'), (64, 553, 103, 83, '54%'), (68, 549, 94, 87, '93%'), (68, 544, 94, 88, '71%'), (65, 544, 96, 94, '72%'), (65, 542, 94, 91, '84%'), (64, 542, 95, 89, '87%'), (65, 539, 90, 88, '93%'), (65, 535, 86, 95, '93%'), (61, 532, 85, 105, '78%'), (62, 532, 85, 98, '78%'), (61, 531, 86, 105, '59%'), (68, 528, 85, 87, '31%'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, (75, 525, 70, 71, '43%'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, (93, 528, 62, 66, '46%'), (93, 529, 63, 64, '52%'), (94, 527, 64, 68, '78%'), (98, 527, 59, 68, '65%'), (97, 528, 60, 68, '71%'), (98, 528, 60, 68, '77%'), (100, 529, 59, 68, '67%'), (102, 530, 55, 66, '38%'), (102, 533, 58, 63, '49%'), (102, 535, 61, 60, '70%'), (102, 535, 61, 61, '82%'), (103, 535, 61, 63, '70%'), (103, 535, 61, 65, '46%'), (103, 534, 70, 64, '50%'), (102, 535, 73, 65, '68%'), (104, 535, 70, 64, '84%'), (105, 536, 69, 62, '68%'), (106, 536, 70, 63, '68%'), (104, 540, 74, 60, '41%'), (105, 539, 74, 61, '30%'), (104, 539, 76, 61, '40%'), (104, 539, 76, 61, '53%'), (105, 539, 76, 61, '58%'), (107, 539, 74, 61, '66%'), (109, 538, 72, 60, '64%'), (109, 538, 73, 60, '47%'), (110, 538, 71, 59, '50%'), (111, 538, 69, 58, '60%'), (109, 537, 71, 59, '66%'), (109, 537, 71, 55, '62%'), (108, 535, 73, 57, '79%'), (111, 534, 69, 56, '92%'), (113, 530, 69, 61, '95%'), (111, 529, 72, 62, '89%'), (116, 527, 68, 66, '78%'), (115, 523, 71, 70, '88%'), (112, 525, 72, 57, '69%'), (113, 522, 72, 59, '48%'), (115, 520, 72, 61, '66%'), (116, 518, 70, 59, '75%'), (121, 515, 66, 61, '59%'), (123, 507, 66, 78, '79%'), (126, 509, 64, 64, '62%'), (128, 504, 66, 60, '89%'), (130, 501, 64, 61, '58%'), (134, 494, 65, 71, '42%'), (134, 493, 68, 63, '27%'), (140, 485, 55, 75, '64%'), None, (142, 483, 67, 56, '72%'), (145, 482, 65, 53, '64%'), (145, 477, 67, 57, '37%'), None, (149, 464, 70, 57, '73%'), (155, 458, 70, 61, '62%'), (161, 453, 68, 61, '82%'), (164, 451, 68, 63, '39%'), (175, 446, 67, 54, '51%'), (175, 444, 71, 55, '61%'), None, None, None, None, None, None, None, None, None, (239, 383, 88, 61, '88%'), (248, 380, 93, 58, '92%'), (254, 378, 95, 57, '82%'), (260, 370, 106, 52, '97%'), (272, 360, 104, 59, '96%'), (276, 354, 113, 64, '95%'), (286, 350, 114, 59, '92%'), (294, 345, 115, 63, '97%'), (316, 334, 103, 68, '97%'), (328, 333, 104, 66, '92%'), (341, 328, 103, 60, '95%'), (351, 321, 102, 64, '97%'), (361, 318, 109, 60, '96%'), (378, 315, 95, 55, '97%'), (384, 308, 102, 60, '97%'), (394, 303, 106, 62, '96%'), (404, 297, 110, 64, '92%'), (419, 293, 103, 58, '98%'), (429, 289, 103, 60, '98%'), (434, 282, 110, 65, '97%'), (447, 276, 113, 67, '96%'), (464, 272, 105, 65, '93%'), (480, 263, 97, 69, '85%'), (485, 260, 106, 70, '95%'), (496, 256, 107, 70, '83%'), (512, 252, 98, 66, '81%'), (521, 251, 101, 63, '97%'), (533, 245, 109, 66, '95%'), (551, 244, 102, 61, '96%'), (557, 240, 105, 63, '34%'), (568, 235, 109, 58, '92%'), (572, 230, 111, 61, '96%'), (594, 222, 99, 67, '97%'), (600, 219, 110, 67, '95%'), (608, 222, 117, 58, '95%'), (626, 212, 101, 63, '97%'), (631, 207, 113, 67, '97%'), (645, 204, 107, 64, '98%'), (659, 199, 106, 68, '97%'), (673, 197, 105, 62, '97%'), (689, 191, 97, 65, '97%'), (697, 189, 100, 65, '97%'), (700, 182, 114, 72, '99%'), (710, 184, 114, 65, '98%'), (724, 180, 112, 66, '98%'), (738, 176, 109, 68, '98%'), (760, 169, 96, 68, '97%'), (769, 167, 93, 70, '98%'), (774, 164, 110, 69, '98%'), (792, 157, 101, 74, '97%'), (800, 154, 105, 77, '95%'), (810, 153, 103, 69, '98%'), (829, 148, 94, 71, '97%'), (833, 144, 116, 76, '98%'), (845, 144, 108, 74, '99%'), (853, 141, 115, 73, '99%'), (869, 138, 109, 75, '99%'), (882, 137, 107, 72, '98%'), (902, 130, 91, 75, '97%'), (910, 125, 101, 78, '98%'), (919, 126, 101, 74, '98%'), (927, 124, 101, 71, '97%'), (942, 116, 105, 81, '97%'), (956, 115, 101, 82, '96%'), (968, 117, 97, 76, '95%'), (980, 112, 100, 74, '95%'), (992, 110, 100, 78, '97%'), (992, 113, 115, 69, '97%'), (1010, 111, 113, 68, '98%'), (1030, 103, 102, 77, '97%'), (1037, 102, 115, 80, '97%'), (1049, 105, 108, 74, '98%'), (1060, 103, 111, 75, '98%'), (1073, 99, 111, 78, '99%'), (1085, 100, 109, 73, '98%'), (1108, 93, 93, 76, '94%'), (1106, 96, 118, 76, '98%'), (1121, 93, 111, 77, '99%'), (1128, 93, 113, 72, '99%'), (1145, 92, 109, 70, '98%'), (1164, 85, 103, 80, '96%'), (1178, 85, 106, 74, '82%'), (1181, 85, 113, 75, '99%'), (1189, 84, 116, 74, '99%'), (1206, 82, 107, 75, '99%'), (1219, 83, 112, 73, '98%'), (1235, 80, 106, 77, '97%'), (1244, 80, 112, 77, '96%'), (1256, 78, 113, 77, '97%'), (1267, 78, 112, 76, '96%'), (1283, 80, 111, 64, '96%'), (1297, 77, 105, 71, '97%'), (1312, 79, 96, 68, '91%'), (1317, 77, 118, 69, '97%'), (1334, 76, 107, 71, '97%'), (1335, 80, 113, 64, '95%'), (1347, 76, 122, 70, '98%'), (1371, 77, 106, 70, '97%'), (1381, 78, 114, 67, '90%'), (1396, 76, 110, 69, '96%'), (1409, 78, 101, 67, '95%'), (1419, 81, 110, 60, '96%'), (1420, 80, 123, 60, '97%'), (1443, 80, 109, 60, '96%'), (1450, 80, 119, 58, '94%'), (1452, 76, 134, 68, '98%'), (1482, 80, 115, 59, '92%'), (1489, 78, 120, 64, '97%'), (1505, 77, 112, 66, '96%'), (1513, 80, 127, 61, '93%'), (1511, 81, 151, 60, '59%'), (1527, 79, 134, 66, '86%'), (1538, 79, 134, 66, '93%'), (1564, 78, 119, 69, '92%'), (1575, 84, 116, 66, '89%'), (1576, 84, 145, 68, '97%'), (1596, 84, 135, 68, '95%'), (1604, 86, 137, 66, '98%'), (1617, 86, 144, 66, '99%'), (1641, 85, 120, 72, '98%'), (1653, 87, 115, 71, '95%'), (1659, 87, 118, 73, '92%'), (1678, 87, 98, 74, '93%'), (1694, 90, 81, 76, '64%'), (1701, 87, 76, 80, '30%'), (1713, 91, 69, 76, '38%'), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    ballx = []
    bally = []
    
    for x in range(len(ball)):
        if (ball[x] == None):
            xpos = None
            ypos = None
        else:
            xpos = ball[x][0]
            ypos = 1920 - ball[x][1]

        ballx.append(xpos)
        bally.append(ypos)

    a=Joint_array(vid.coord_array)
    handx = a.wrist_x
    handy = a.wrist_y

    #X COORDINATE STUFF
    xdist = []
    for x in range(len(ball)):
      if (ball[x] == None):
            c = None
      else:
            c = abs(handx[x]-ballx[x])
      xdist.append(c)

    #plt.plot(xdist)
    #plt.title('distance between x-coordiante of wrist and ball')
    #plt.show()

    #creating ball xdist without none
    if (ball[x] == None):
      xdist[0] = 0
    else:
      xdist[0] = xdist[0]

    for x in range(1,len(xdist)):
       if (xdist[x] == None):
         xdist[x] = xdist[x-1]

    #xcoord thershold
    rt1 = []
    for x in range(4,len(xdist)):
      if xdist[x] > xdist[x-5]+30:
        rt1.append(x)
    
    print("x threshold release time is frame", rt1[0])

    #slope of x distance
    d_xdist = [0]
    for x in range(1,len(xdist)-1):
      m = (xdist[x-1]+xdist[x+1])/2
      d_xdist.append(m)
    #plt.plot(d_xdist)
    #plt.title("rate of change of distance between x-coordinates")
    #plt.show()

    rt2 = []
    for x in range(4,len(d_xdist)):
      if d_xdist[x] > d_xdist[x-5]+35:
        rt2.append(x)
    print("x distance slope release time is frame", rt2[0])

    #Y COORDINATE STUFF
    ydist = []
    for x in range(len(ball)):
      if (ball[x] == None):
            c = None
      else:
            c = abs(handy[x]-bally[x])
      ydist.append(c)

    #plt.plot(ydist)
    #plt.title('distance between y-coordiante of wrist and ball')
    #plt.show()
    
    #creating ball ydist without none
    if (ball[x] == None):
      ydist[0] = 0
    else:
      ydist[0] = ydist[0]

    for x in range(1,len(ydist)):
       if (ydist[x] == None):
         ydist[x] = ydist[x-1]

    #ycoord thershold
    rt3 = []
    for x in range(4,len(ydist)):
      if ydist[x] > ydist[x-5]+40:
        rt3.append(x)
    
    print("y threshold release time is frame", rt3[0])

    #slope of y distance
    d_ydist = [0]
    for x in range(1,len(ydist)-1):
      m = (ydist[x-1]+ydist[x+1])/2
      d_ydist.append(m)
    #plt.plot(d_ydist)
    #plt.title("rate of change of distance between y-coordinates")
    #plt.show()

    rt4 = []
    for x in range(4,len(d_ydist)):
      if d_ydist[x] > d_ydist[x-5]+35:
        rt4.append(x)
    print("y distance slope release time is frame", rt4[0])

    #DISTANCE BETWEEN POINTS STUFF
    distance = []
    for x in range(len(ball)):
      if (ball[x] == None):
            c = None
      else:  
            c = math.sqrt((ballx[x]-handx[x])**2+(bally[x]-handy[x])**2)
      distance.append(c)
     
    #creating distance without nones
    if (ball[x] == None):
      distance[0] = 0
    else:
      distance[0] = distance[0]
          
    for x in range(1,len(distance)):
       if (distance[x] == None):
         distance[x] = distance[x-1]
    #slope of distance
    d_distance = [0]
    for x in range(1,len(distance)-1):
      m = (distance[x-1]+distance[x+1])/2
      d_distance.append(m)
    #plt.plot(d_distance)
    #plt.show()

    rt5 = []
    for x in range(4,len(d_distance)):
      if d_distance[x] > d_distance[x-5]+35:
        rt5.append(x)
    print("distance slope release time is frame", rt5[0])
    

    #distance threshold
    rt6 = []
    for x in range(4,len(distance)):
      if distance[x] > distance[x-5]+35:
        rt6.append(x)
    print("distance threshold release time is frame", rt6[0])

    rt = [rt1[0], rt2[0], rt3[0], rt4[0], rt5[0], rt6[0]]
    rt = list(rt)
    rel_time = statistics.median(rt) - 10
    vid.t3=int(rel_time)
    print("relase time is", rel_time)
