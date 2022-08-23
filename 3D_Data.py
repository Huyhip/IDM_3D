from InvidistModule import *
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
import matplotlib.pyplot as plt

# xv_in = [60.0, 61.0, 62.0, 62.5, 63.0, 61.0, 61.5, 62.0, 62.5, 63.0, 2.5, 6.25, 12.5, 18.75, 25.0, 31.25, 37.5, 43.75, 50.0, 56, 0, 7, 14, 21, 28, 42, 49, 56, 60, 63]
# yv_in = [3, 6, 9, 12, 15, 88, 92, 96, 100, 110, 12.5, 25.0, 31.25, 37.5, 50.0, 56.25, 62.5, 75.0, 87.5,90 , 100, 113, 114, 115, 117, 119, 121, 123, 125, 127]
# zv_in = [0.5,0.75,1,1.25,1.5,0.5,0.75,1,1.25,1.5,0.5,1,1.5,2,2.5,3,3.5,3,2,2.5,0.5,1,0.5,1,0.5,1,0.5,1,0.5,1]
# values_in = [10,10,10,10,10,13,14,14,13,14,1,2,0,1,1,0,0,1,2,1,12,12,12,12,12,12,12,12,12,12]

# save(invDist_in(xv_in,yv_in,zv_in,values_in,1,64,128), 20)

# xv = [21.003043230448874,21.002929342416156,21.002845491787347,21.00271770518014,21.002684197567515 ,21.00279212202684,
#             21.002575942150735,21.003053301544917,21.002523578354193,21.002954665705076,21.002611235756707,21.003074369393424,
#             21.003015025835904,21.0026437974515 ,21.002913759393774,21.003115792402525, 21.002901241100343,21.00259546965901,
#             21.002784609525325,21.003015025835904]
# yv = [105.84589232742832,105.84590956090776,105.84579485275937,105.84578070752619,105.8459052500942,105.84554872729501,
#             105.84530129465635,105.84542886054284,105.84540782637767,105.84549637951034,105.84561747515856,105.84549387178383,
#             105.84549387178383,105.84547333577046,105.84556730365114,105.843115792402525,105.84596062573516,105.8459425394196,
#             105.8452762376456,105.8452762376456]
# zv = [10,12,4,13,16,17,9,12,1,16,12,11,9,8,18,6,7,1,3,7]
# values = [0.2,0.1,0.6,0.2,0.2,0.3,0.1,0.2,0.1,0.3,0.1,0.6,0.4,0.2,0.5,0.1,0.3,0.2,0.3,0.4]
# invDist_out(xv,yv,zv,values,1,64,64)

# img = cv2.imread("./Images/db.png")
# point(img,512,256,9.15,4.25)

# Data1:
# xv = [0,5,10,15,20,25,30,26,23,17,8,16,3,2,1,40,45,31,35,52,25,30,35,40,45,50,55,60,62,63,2,3,4,5,6,50,52,54,56,60]
# yv = [2,3,5,7,10,12,15,20,22,19,17,12,0.5,0.5,0.5,45,50,55,60,62,43,63,45,44,63,60,55,52,51,50,62,1,3,7,1,2,2,4,6,7,10]
# zv = [18,5,6,1,7,3,6,12,8,10,12,14,15,17,20,43,45,57,54,63,43,55,57,47,60,55,50,45,44,63,63,60,62,61,60,2,4,6,10,3]
# values = [15,17,15,17,18,17,16,16,16,15,14,17,16,17,15,1,1,1,1,1,2,5,1,2,2,2,3,1,3,3,10,12,13,12,10,1,2,3,1,1]

# # Data2:
# xv = [0,5,10,15,20,25,30,26,23,17,8,16,3,2,1,40,45,31.5,35,52,25,30,35,40,45.5,50,55,60,62,63,2,3,4,5,6,50,52,54,56,60]
# yv = [2,3,5,7,10,12,15,20,22,19,17,12,0.5,0.5,0.5,45.5,50,55.5,60,62,43,63,45,44,63,60,55,52,51,50,62,1,3,7,1,2,2,4,6,7,10]
# zv = [18,5,6,1,7,3,6,12,8,10,12,14,15,17,20,43,45,57,54,63,43,55,57,47,60,55,50,45,44,63,63,60,62,61,60,2,4,6,10,3]
# values = [1,1,1,1,1,2,5,1,2,2,2,3,1,3,3,18,17,20,17,18,17,16,16,16,20,14,17,16,17,15,10,12,13,12,10,1,2,3,1,1]

# Data3:
xv = [20,25,30,35,40,22,27,32,37,45,23.5,26.5,31.5,36.5,40.5  ,40,45,31.5,35,52,25,30,35,40,45.5,50,55,60,62,63,  12,23,14,15,16   ,5,15,25,35,40,45,50,55,57,58,60,62,62.5,47,36,25,15,7,2,3,4,5.5,3.2,6.2,5]
yv = [21,24,31,36,41,23,27.5,32.5,37.5,45.5,23.5,26.5,31.5,36.5,40.5  ,2,3,5,7,10,12,15,20,22,19,17,12,0.5,0.5,0.5  ,12,21,13,15,11     ,1,12,6,7,5,6,7,5,15,25,30,36,40,55,60,62.4,57,58,59,60,55.5,34.5,23.7,12,5]
zv = [23,24,25,26,28,30,32,34,37,40,43,45.6,32.5,35.6,40.5  ,2,3,5,7,1.6,2.6,1.5,2.8,2.2,1.9,1.7,1.2,0.5,0.5,0.5   ,63,60.1,62,61.5,60.5     ,5,10,15,20,25,30,35,40,45,50,55,60,62,5,10,15,20,25,30,35,40,45,50,55,60]
values = [17,18,17,18,19,20,18,17,18,18,17,19,17,18,19   ,2,3,2,3,1,1,3,1,1,2,1,3,1,3,3    ,7,8,7,9,7     ,8,7,14,7,6,7,10,4,7,1,4,9,7,12,3,4,10,2,8,7,4,12,7,4,8]


for i in range(0,13,1):

    save(invDist_in(xv,yv,zv,values,zi=i*5,xsize = 64,ysize = 64),20,i)

    print(i)

# xv_in = [60.0, 61.0, 62.0, 62.5, 63.0, 61.0, 61.5, 62.0, 62.5, 63.0, 2.5, 6.25, 12.5, 18.75, 25.0, 31.25, 37.5, 43.75, 50.0, 56, 0, 7, 14, 21, 28, 42, 49, 56, 60, 63]

# yv_in = [3, 6, 9, 12, 15, 88, 92, 96, 100, 110, 12.5, 25.0, 31.25, 37.5, 50.0, 56.25, 62.5, 75.0, 87.5,90 , 100, 113, 114, 115, 117, 119, 121, 123, 125, 127]

# zv_in = [0.5,0.75,1,1.25,1.5,0.5,0.75,1,1.25,1.5,0.5,1,1.5,2,2.5,3,3.5,3,2,2.5,0.5,1,0.5,1,0.5,1,0.5,1,0.5,1]

# values_in = [10,10,10,10,10,13,14,14,13,14,1,2,0,1,1,0,0,1,2,1,12,12,12,12,12,12,12,12,12,12]

# save(invDist_in(xv_in,yv_in,zv_in,values_in,1,64,128), 20, 1)