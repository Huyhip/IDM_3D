from math import pow
import cv2
from math import sqrt
import numpy as np
from matplotlib import cm


def pointValue(x,y,z,power,smoothing,xv,yv,zv,values):
    nominator=0
    denominator=0
    for i in range(0,len(values)):
        dist = sqrt((x-xv[i])*(x-xv[i])+(y-yv[i])*(y-yv[i])+(z-zv[i])*(z-zv[i])+smoothing*smoothing)
        if(dist<0.0000000001):
            return values[i]
        nominator=nominator+(values[i]/pow(dist,power))
        denominator=denominator+(1/pow(dist,power))
    if denominator > 0:
        value = nominator/denominator
    else:
        value = -9999
    return value

def invDist(xv,yv,zv,xi,yi,zi,values,xsize=100,ysize=100,power=2,smoothing=0):
    valuesGrid = np.zeros((ysize,xsize))
    for x in range(0,xsize):
        for y in range(0,ysize):
            valuesGrid[y][x] = pointValue(xi[x],yi[y],zi,power,smoothing,xv,yv,zv,values)
    return valuesGrid
    
def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

def ConvertRange(old_value,old_min,old_max,new_min,new_max):
    return ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min

power=1
smoothing=20

#Make layer 1:
xv = [10,60,40,70,10,50,20,70,30,60,10.1,30.2,50.3,80.4,90.5,32.1,42.2,12.3,62.4,52.5]
yv = [10,20,30,30,40,50,60,70,80,90,23.1,24.3,25.2,23.2,35.2,68.1,70.1,34.1,68.2,70.5]
zv = [10,12,4,13,16,17,9,12,1,16,12,11,9,8,18,6,7,1,3,7]
values = [1,8,2,3,4,3,4,8,7,1,5,3,8,6,2,5,5,1,3,10]
    
n=64 #size pic
zi=1 #do cao layer can tinh
xi = np.linspace(min(xv),max(xv) , n)
yi = np.linspace(min(yv),max(yv) , n) 
layer1 = invDist(xv,yv,zv,xi,yi,zi,values,n,n,power,smoothing)

#normalize matrix to (0,1)
normalized_matrix =  NormalizeData(layer1)
#print(normalized_matrix)

#convert from range(0,1) to range (0.5 , 0.9)
convert_to_range_05_09 = ConvertRange(normalized_matrix,0,1,0.5,0.9)
#print(convert_to_range_05_09)

viridis_big = cm.get_cmap('nipy_spectral')
print("----------")

#get the value of 'nipy_spectral' color
matrix_color = viridis_big(convert_to_range_05_09)

#remove the 4th values which is = 1
matrix_color2 = matrix_color[:,:,:3]

#multiple matrix with 255 to get the color RGB value matrix
matrix_color3 = matrix_color2*255

#write the matrix to an image
cv2.imwrite('D:/Lab/Invdist/Images/color_img_1.png', matrix_color3)

#cv2.imwrite
#read image
img = cv2.imread("D:/Lab/Invdist/Images/color_img_1.png")

#convert image from RGB to BGR
matrix_color4 = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

#save the image
cv2.imwrite('D:/Lab/Invdist//Images/Layer1.png', matrix_color4)