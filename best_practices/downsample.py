
import os, sys
import numpy as np
from time import time

# This function downsamples a certain image by getting the mean in a certain cell shape
def downsample(x, cell):
    c0, c1 = cell
    yshape = (x.shape[0] // c0, x.shape[1] // c1)
    y = np.empty(yshape, x.dtype)
    for i in range(yshape[0]):
        for j in range(yshape[1]):
            y[i, j] = x[i*c0:(i+1)*c0,j*c1:(j+1)*c1].mean()
    return y

# Create a sample image
if len(sys.argv) > 1:
    img_shape = int(sys.argv[1]), int(sys.argv[2])
else:
    img_shape = 2**24
img = np.arange(img_shape[0]*img_shape[1], dtype=np.float32).reshape(img_shape)
t0 = time()
dsimg = downsample_(img, (16,16))
print("The time for downsampling: %.3f" % (time() - t0))
print("Initial shape: %s.  Final shape: %s" % (img.shape, dsimg.shape))  