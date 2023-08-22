#!/usr/bin/env python3
"""
1st gen flight scaling concept 
"""

__author__ = "Chase Marino"
__version__ = "0.1.0"

import matplotlib.pyplot as plt
from contextlib import nullcontext
from hashlib import blake2b
import random




def main():
    """ Main entry point of the app """
    initCoords = [[-10, 0], [24, 0], [23, 19], [0, 64]]

    coords = [(random.random()*10000.0, random.random()*10000.0) for _ in range(50)]

    # (-100, 0)(24, 0)(12, 15)(0, 78)
    bottom = 9999999
    top = -9999999
    left = 9999999
    right = -9999999

    for curr in coords:
        plt.scatter(x=curr[0], y=curr[1])
        if (curr[0] < left):
            left = curr[0]
        if (curr[0] > right):
            right = curr[0]

        if (curr[1] < bottom):
            bottom = curr[1]
        if (curr[1] > top):
            top = curr[1]

    rectangle = plt.Rectangle((left,bottom), right - left, top - bottom, alpha = .2, fc='blue',ec="red")
    plt.gca().add_patch(rectangle)

    #Flight zone defs -- centering in current plane for testing
    zonetl = [5000, 5500]
    zonetr = [5500, 5500]
    zonebl = [5000, 5000]
    zonebr = [5500, 5000]

    #possible solution to find scaling factor - find difference x && difference in y 
    x_dist = (right - left)
    y_dist = (top - bottom)

    zone_x = zonebr[0] - zonebl[0]
    x_scale = zone_x / x_dist
    zone_y = zonetr[1] - zonebr[1]
    y_scale = zone_y / y_dist

    print("scales")
    print(x_scale)
    print(y_scale)
    
    for curr in coords:
        #curr
        scf_x = left
        cx = zonebl[0] + ((curr[0] - left) * x_scale)
        cy = zonebr[1] + ((curr[1] - bottom) * y_scale)
        
        plt.scatter(x=cx, y=cy, color='black')



    flightBounds = plt.Rectangle(zonebl, zonetr[0] - zonetl[0], zonetr[1] - zonebl[1], alpha = .5, fc='black',ec="red")
    plt.gca().add_patch(flightBounds)
    

    plt.show()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()