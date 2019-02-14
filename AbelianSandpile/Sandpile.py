#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:16:14 2019

@author: ben
"""

import numpy as np
import matplotlib.pyplot as plt

MAXD = 4
WIDTH = 100
HEIGHT = 100
DROP = (int(WIDTH/2), int(HEIGHT/2))
P = 5000
GRID = np.zeros((WIDTH, HEIGHT), dtype=np.uint8)

def drop(grid, x, y):
    grid[x,y] += 1
    if(grid[x,y] >= MAXD):
        grid[x,y] = 0
        drop(grid, x+1, y)
        drop(grid, x-1, y)
        drop(grid, x, y+1)
        drop(grid, x, y-1)
        
def start(grid, x, y, iterations=100):
    for _ in range(0, iterations):
        drop(GRID, x, y)
        
def to_image(grid, colors):
    img = np.zeros((grid.shape[0], grid.shape[1], 3))
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            img[i,j,:] = colors[grid[i,j]]
    return img


start(GRID, DROP[0], DROP[1], P)
np.savetxt("grid.csv", GRID, delimiter=",")
plt.imshow(GRID, interpolation='none')