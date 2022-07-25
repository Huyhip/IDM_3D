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

def invDist3d(xv,yv,zv,xi,yi,zi,values,xsize=100,ysize=100,zsize=100, power=2,smoothing=0):
    valuesGrid = np.zeros((zsize,ysize,xsize))
    for x in range(0,xsize):
        for y in range(0,ysize):
            for z in range(0,zsize):
                valuesGrid[z][y][x] = pointValue3d(xi[x],yi[y],zi[z],power,smoothing,xv,yv,zv,values)
    return valuesGrid

if __name__ == "__main__":
    power=1
    smoothing=20

    #Creating some data, with each coodinate and the values stored in separated lists
    xv = [10,60,40,70,10,50,20,70,30,60,10.1,30.2,50.3,80.4,90.5,32.1,42.2,12.3,62.4,52.5]
    yv = [10,20,30,30,40,50,60,70,80,90,23.1,24.3,25.2,23.2,35.2,68.1,70.1,34.1,68.2,70.5]
    zv = [10,12,4,13,16,17,9,12,1,16,12,11,9,8,18,6,7,1,3,7]
    values = [1,8,2,3,4,3,4,8,7,1,5,3,8,6,2,5,5,1,3,10]
      
    #Creating the output grid
    n=64 #so diem can anh xa = n^3
    xi = np.linspace(min(xv), max(xv) , n)
    yi = np.linspace(min(yv), max(yv) , n)
    zi =np.linspace(min(zv),max(zv),n)
    #print(zi)
    XI,YI=np.meshgrid(xi,yi)

    #Creating the interpoxion function and popuxing the output matrix value
    VI = invDist3d(xv,yv,zv,xi,yi,zi,values,n,n,n,power,smoothing)

    # Plotting the result
    viridis_big = cm.get_cmap('nipy_spectral')
    newcmp = ListedColormap(viridis_big(np.linspace(0.5, 0.9)))
    # for i in range(0,n):
    #     t=plt.pcolor(xI, yI, VI[i], cmap=newcmp)
    #     ax = plt.gca()
    #     ax.axes.xaxis.set_ticks([])
    #     ax.axes.yaxis.set_ticks([])
    #     extent = ax.get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())
    #     plt.savefig("cut{}".format(i), bbox_inches=extent)
    t=plt.pcolor(XI, YI, VI[0], cmap=newcmp)
    ax = plt.gca()
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])
    extent = ax.get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())
    plt.savefig("D:/Lab/Invdist/Images/cut_0.png", bbox_inches=extent)
    #plt.scatter(xv, yv, 10, values)
    #plt.xlim(0, 10)
    #plt.ylim(0, 10)
    #plt.colorbar(t)
    #plt.show()