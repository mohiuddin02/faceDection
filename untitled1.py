# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 12:28:09 2020

@author: mohiu
"""

from skimage import io as skio
url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Convex_lens_%28magnifying_glass%29_and_upside-down_image.jpg/341px-Convex_lens_%28magnifying_glass%29_and_upside-down_image.jpg'
img = skio.imread(url)
print("shape of image: {}".format(img.shape))
print("dtype of image: {}".format(img.dtype))
from skimage import filters
sobel = filters.sobel(img)

import matplotlib.pyplot as plt
#%matplotlib inline
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['figure.dpi'] = 200

plt.imshow(sobel)


blurred = filters.gaussian(sobel, sigma=2.0)
plt.imshow(blurred)



blurredimg = filters.gaussian(img, sigma=2.0)
plt.imshow(blurredimg)
plt.imshow(img)
