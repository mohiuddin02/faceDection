# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:45:01 2020

@author: mohiu
"""

import cv2 as cv 
from matplotlib import pyplot as plt 
  
# read left and right images 
imgR = cv.imread('http://i.stack.imgur.com/SYxmp.jpg', 0) 
imgL = cv.imread('left.png', 0) 
  
# creates StereoBm object  
stereo = cv.StereoBM_create(numDisparities = 16, 
                            blockSize = 15) 
  
# computes disparity 
disparity = stereo.compute(imgR) 
  
# displays image as grayscale and plotted 
plt.imshow(disparity, 'gray') 
plt.show() 