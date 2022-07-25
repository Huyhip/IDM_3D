from math import pow
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri

def pointValue3d(x,y,z,power,smoothing,xv,yv,zv,values):
    nominator=0
    denominator=0
    c=1.113195e5
    for i in range(0,len(values)):
        dist = sqrt((x-xv[i])**2+(y-yv[i])**2+(z-zv[i])**2+smoothing*smoothing)
        if(dist<0.0000000001):
            return values[i]
        nominator=nominator+(values[i]/pow(dist,power))
        denominator=denominator+(1/pow(dist,power))
    if denominator > 0:
        value = nominator/denominator
    else:
        value = -9999
    return value

def invDist3d(xv,yv,zv,xi,yi,zi,values,xsize=100,ysize=100,zsize=100, power=2,smoothing=0):
    valuesGrid = np.zeros((zsize,ysize,xsize))
    for y in range(0,xsize):
        for x in range(0,ysize):
            for z in range(0,zsize):
                valuesGrid[y][x][z] = pointValue3d(xi[x],yi[y],zi[z],power,smoothing,xv,yv,zv,values)
    return valuesGrid

if __name__ == "__main__":
    power=1
    smoothing=20

    #Creating some data, with each coodinate and the values stored in separated lists
    # xv = [21.003043230448874,21.002929342416156,21.002845491787347,21.00271770518014,21.002684197567515 ,21.00279212202684,
    #         21.002575942150735,21.003053301544917,21.002523578354193,21.002954665705076,21.002611235756707,21.003074369393424,
    #         21.003015025835904,21.0026437974515 ,21.002913759393774,21.003115792402525, 21.002901241100343,21.00259546965901,
    #         21.002784609525325,21.003015025835904]
    # yv = [105.84589232742832,105.84590956090776,105.84579485275937,105.84578070752619,105.8459052500942,105.84554872729501,
    #         105.84530129465635,105.84542886054284,105.84540782637767,105.84549637951034,105.84561747515856,105.84549387178383,
    #         105.84549387178383,105.84547333577046,105.84556730365114,105.843115792402525,105.84596062573516,105.8459425394196,
    #         105.8452762376456,105.8452762376456]
    # zv = [10,12,4,13,16,17,9,12,1,16,12,11,9,8,18,6,7,1,3,7]
    # values = [0.2,0.1,0.6,0.2,0.2,0.3,0.1,0.2,0.1,0.3,0.1,0.6,0.4,0.2,0.5,0.1,0.3,0.2,0.3,0.4]

    xv = [10,60,40,70,10,50,20,70,30,60,10.1,30.2,50.3,80.4,90.5,32.1,42.2,12.3,62.4,52.5]
    yv = [10,20,30,30,40,50,60,70,80,90,23.1,24.3,25.2,23.2,35.2,68.1,70.1,34.1,68.2,70.5]
    zv = [10,12,4,13,16,17,9,12,1,16,12,11,9,8,18,6,7,1,3,7]
    values = [1,8,2,3,4,3,4,8,7,1,5,3,8,6,2,5,5,1,3,10]
      
    #Creating the output grid
    n=64 #so diem can anh xa = n^3
    xi = np.linspace(min(xv), max(xv) , n)
    yi = np.linspace(min(yv), max(yv) , n)
    zi =np.linspace(min(zv),max(zv),n)
    XI,YI,ZI=np.meshgrid(xi,yi,zi)

    #Creating the interpoxion function and popuxing the output matrix value
    VI = invDist3d(xv,yv,zv,xi,yi,zi,values,n,n,n,power,smoothing)
    #print(VI)

    # Plotting the result
    viridis_big = cm.get_cmap('nipy_spectral')
    newcmp = ListedColormap(viridis_big(np.linspace(0.5, 0.9)))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    v=ax.scatter(XI, YI, ZI, c=VI, cmap=newcmp,alpha=0.3)
    #plt.colorbar(v)
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    plt.savefig('D:/Lab/Invdist/Images/3D.png')
    #plt.show()