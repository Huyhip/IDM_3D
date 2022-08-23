from math import pow
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri

def pointValue3d(x,y,z,power,xv,yv,zv,values):
    nominator=0
    denominator=0
    c=1.113195e5
    for i in range(0,len(values)):
        dist = sqrt((x-xv[i])*(x-xv[i])+(y-yv[i])*(y-yv[i])+(z-zv[i])*(z-zv[i]))
        if(dist<0.0000000001):
            return values[i]
        nominator=nominator+(values[i]/pow(dist,power))
        denominator=denominator+(1/pow(dist,power))
    if denominator > 0:
        value = nominator/denominator
    else:
        value = -9999
    return value

def invDist3d(xv,yv,zv,xi,yi,zi,values,xsize=100,ysize=100,zsize=100, power=2):
    valuesGrid = np.zeros((zsize,xsize,ysize))
    for x in range(0,xsize):
        for y in range(0,ysize):
            for z in range(0,zsize):
                valuesGrid[z][x][y] = pointValue3d(xi[x],yi[y],zi[z],power,xv,yv,zv,values)
    return valuesGrid

if __name__ == "__main__":
    power=1

    #Creating some data, with each coodinate and the values stored in separated lists
    # xv = [0,5,10,15,20,25,30,35,40,45,50,55,60,62,63,0,5,10,15,20,25,30,35,40,45,50,55,60,62,63]
    # yv = [0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,63,54,52,10,13,17,30,44,33,22,10,7,2,27,39]
    # zv = [0,6,12,18,24,30,36,42,48,54,60,40,46,52,63,3,5,7,14,18,33,55,32,52,63,2,7,18,10,1]
    # values = [14,7,6,3,2,15,14,2,10,3,4,1,10,9,15,7,8,4,10,14,17,2,4,4,3,10,15,13,7,1]

    xv = [20,25,30,35,40,22,27,32,37,45,23.5,26.5,31.5,36.5,40.5  ,40,45,31.5,35,52,25,30,35,40,45.5,50,55,60,62,63,  12,23,14,15,16   ,5,15,25,35,40,45,50,55,57,58,60,62,62.5,47,36,25,15,7,2,3,4,5.5,3.2,6.2,5]
    yv = [21,24,31,36,41,23,27.5,32.5,37.5,45.5,23.5,26.5,31.5,36.5,40.5  ,2,3,5,7,10,12,15,20,22,19,17,12,0.5,0.5,0.5  ,12,21,13,15,11     ,1,12,6,7,5,6,7,5,15,25,30,36,40,55,60,62.4,57,58,59,60,55.5,34.5,23.7,12,5]
    zv = [23,24,25,26,28,30,32,34,37,40,43,45.6,32.5,35.6,40.5  ,2,3,5,7,1.6,2.6,1.5,2.8,2.2,1.9,1.7,1.2,0.5,0.5,0.5   ,63,60.1,62,61.5,60.5     ,5,10,15,20,25,30,35,40,45,50,55,60,62,5,10,15,20,25,30,35,40,45,50,55,60]
    values = [17,18,17,18,19,20,18,17,18,18,17,19,17,18,19   ,2,3,2,3,1,1,3,1,1,2,1,3,1,3,3    ,7,8,7,9,7     ,8,7,14,7,6,7,10,4,7,1,4,9,7,12,3,4,10,2,8,7,4,12,7,4,8]
    print(len(xv))
    print(len(yv))
    print(len(zv))
    print(len(values))

    

    #Creating the output grid
    n=64 #so diem can anh xa = n^3
    xi = np.linspace(0, n-1, n)
    yi = np.linspace(0, n-1, n)
    zi = np.linspace(0, n-1, n)


    #Creating the interpoxion function and popuxing the output matrix value
    VI = invDist3d(xv,yv,zv,xi,yi,zi,values,n,n,n,power)
    viridis_big = cm.get_cmap('nipy_spectral')
    newcmp = ListedColormap(viridis_big(np.linspace(0.5, 0.9)))

    # XI,YI=np.meshgrid(xi,yi)
    # t=plt.pcolor(XI, YI, VI[30], cmap=newcmp,vmin=0,vmax=20)
    # ax = plt.gca()
    # ax.axes.xaxis.set_ticks([])
    # ax.axes.yaxis.set_ticks([])
    # extent = ax.get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())
    # plt.savefig("./Images/cut_0.png", bbox_inches=extent)


    XI,YI,ZI=np.meshgrid(xi,yi,zi)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    v=ax.scatter(XI, YI, ZI, c=VI, cmap=newcmp,vmin=0,vmax=20 )
    # ax.grid(False)
    # ax.set_xticks([])
    # ax.set_yticks([])
    # ax.set_zticks([])
    plt.savefig('./Images/plot_3D.png')

    #plt.colorbar(t)
    #plt.show()