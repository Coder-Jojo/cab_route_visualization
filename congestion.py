import math
import numpy as np

def congestion_array(rows,cols):
    random_array = abs(np.random.normal(0, 0.5, rows*cols))
    return random_array
    #for i in range(100):
     #   for j in range(100):
      #      grid.update_cell(i,j,(255, 255 - min(255,math.floor(255*random_array[i*100 + j])), 255 - min(255,math.floor(255*random_array[i*100 + j]))))

def color_ret(random_array,i,j):
    return 255, 255 - min(255,math.floor(255*random_array[i*100 + j])), 255 - min(255,math.floor(255*random_array[i*100 + j]))