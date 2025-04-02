import numpy as np
from time import time
import matplotlib
# the following will prevent the figure from popping up
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def simple_mandelbrot(width, height, real_low, real_high, imag_low, imag_high, max_iters):
    real_vals = np.linspace(real_low, real_high, width) # defining x real axis
    imag_vals = np.linspace(imag_low, imag_high, height) # defining y imaginary axis
    
    # we will represent memebrs of Mandelbrot as 1, non members as 0
    
    mandelbrot_graph = np.ones((height, width), dtype=np.float32)
    
    for x in range(width):
        for y in range(height):
            
            c = np.complex64( real_vals[x] + imag_vals[y]*1j)
            z= np.complex64(0)
            
            for i in range(max_iters):
                
                z = z**2 + c
                
                if (np.abs(z) > 2):
                    mandelbrot_graph[y,x] = 0
                    break
                
    return mandelbrot_graph
            


if __name__ == '__main__':
    
    t1 = time()
    mandel = simple_mandelbrot(512, 512, -2, 2, -2, 2, 256)
    t2 = time()
    
    mandel_time = t2 - t1
    
    
    t1 = time()
    fig = plt.figure(1)
    plt.imshow(mandel, extent=(-2, 2, -2, 2))
    plt.savefig('mandelbrot.png', dpi=fig.dpi)
    t2 = time()
    
    dump_time = t2-t1
    
    print(f"It took {mandel_time} seconds to calculate the Mandelbrot set")
    print(f"It took {dump_time} seconds to dump the image")
    