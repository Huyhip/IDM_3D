from math import pow
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap

def pointValue(x,y,power,smoothing,xv,yv,values):
    nominator=0
    denominator=0
    for i in range(0,len(values)):
        dist = sqrt((x-xv[i])*(x-xv[i])+(y-yv[i])*(y-yv[i])+smoothing*smoothing)
        #If the point is really close to one of the data points, return the data point value to avoid singularities
        if(dist<0.0000000001):
            return values[i]
        nominator=nominator+(values[i]/pow(dist,power))
        denominator=denominator+(1/pow(dist,power))

    #Return NODATA if the denominator is zero
    if denominator > 0:
        value = nominator/denominator
    else:
        value = -9999
    return value

def invDist(xv,yv,values,xsize=100,ysize=100,power=2,smoothing=0):
    valuesGrid = np.zeros((ysize,xsize))
    for x in range(0,xsize):
        for y in range(0,ysize):
            valuesGrid[y][x] = pointValue(x,y,power,smoothing,xv,yv,values)
    return valuesGrid

    
if __name__ == "__main__":
    power=10
    smoothing=20

    #Creating some data, with each coodinate and the values stored in separated lists
    xv = [51.2, 307.2, 204.8, 358.4, 51.2, 256, 102.4, 358.4, 153.6, 307.2, 51.7, 154.6, 257.5, 411.6, 463.3, 164.3, 216, 63, 319.5, 268.8]
    yv = [51.2, 102.4, 153.6, 153.6, 204.8, 256, 307.2, 358.4, 409.6, 460.8, 118.3, 124.4, 129, 118.7, 180.2, 348.6, 359, 174.5, 350, 361]
    values = [1,8,2,6,4,3,4,8,7,1,5,3,8,6,2,9,9,1,3,10]

    # xv = [10,60,40,70,10,50,20,70,30,60,10.1,30.2,50.3,80.4,90.5,32.1,42.2,12.3,62.4,52.5]
    # yv = [10,20,30,30,40,50,60,70,80,90,23.1,24.3,25.2,23.2,35.2,68.1,70.1,34.1,68.2,70.5]
    # values = [1,8,2,3,4,3,4,8,7,1,5,3,8,6,2,5,5,1,3,10]
     
    #Creating the output grid (100x100, in the example)
    n=512
    xi = np.linspace(min(xv),max(xv) , n)
    yi = np.linspace(min(yv),max(yv) , n)
    XI, YI = np.meshgrid(xi, yi)

    #Creating the interpolation function and populating the output matrix value
    ZI = invDist(xv,yv,values,n,n,power,smoothing)
    #print(ZI)


    # Plotting the result
    viridis_big = cm.get_cmap('nipy_spectral')
    newcmp = ListedColormap(viridis_big(np.linspace(0.5, 0.9)))
    t=plt.pcolor(XI, YI, ZI, cmap=newcmp)
    plt.scatter(xv, yv, 100, values)
    #plt.xlim(0, 10)
    #plt.ylim(0, 10)
    #plt.colorbar(t)
    # ax = plt.gca()
    # ax.axes.xaxis.set_ticks([])
    # ax.axes.yaxis.set_ticks([])
    # extent = ax.get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())
    # plt.savefig('t1.png', bbox_inches=extent)

    # xline = [7, 10]
    # yline = [10, 2]
    # plt.plot(xline, yline, color="white", linewidth=3)

    plt.show()