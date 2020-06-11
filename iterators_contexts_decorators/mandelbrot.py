
# Make a plot of the mandelbrot set
import numpy as np
from matplotlib import pylab as plt
from matplotlib import cm

# Test a given x,y coordinate to see if it's a member of the set
def in_mandelbrot(x0, y0, n):
    x = 0
    y = 0
    while n > 0:
        xtemp = x * x - y * y + x0
        y = 2 * x * y + y0
        x = xtemp
        n -= 1
        if x * x + y * y > 4:
            return False
    return True

# Generate a range of floating point numbers 
def frange(fmin,fmax,divisions):
    delta = (fmax - fmin)/divisions
    x = fmin
    for i in range(divisions):
        yield x
        x += delta

# Generate all of the pixels of the mandelbrot set.  The output of
# this function is a sequence of rows.  Each row is a sequence of
# True/False values indicating whether or not a point is a member
# of the set or not. Note: This is using generators and generator
# expressions to produce all of the pixels without ever allocating
# a huge array of pixels in memory. 
def generate_mandel(xmin=-2.0, ymin=-1.5, width=3.0, height=3.0, pixels=128, n=400):
    for y in frange(ymin, ymin + height, pixels):
        for x in frange(xmin, xmin + width, pixels):
            yield in_mandelbrot(x, y, n)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        npixels = int(sys.argv[1])
    else:
        npixels = 128
    img = generate_mandel(pixels=npixels)
    im = np.fromiter(img, dtype=bool).reshape(npixels, npixels)
    plt.imshow(im, cmap=cm.gray_r)
    plt.show()