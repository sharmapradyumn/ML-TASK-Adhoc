#!/usr/bin/python3

import numpy as np

# array between fixed range

x= np.arange(100,200,5) #array between 100 to 200 with difference of 5
print("array between 100 to 200   :\n",x)

y= x[0:16].reshape(8,2) # its print 8,2 array ,,,,x[0:16] slice the array first than we convert it into 8,2

z=x.reshape(10,2) # without slicing its cant reshape the array in 8,2 but it can be in 10,2

print("8*2 array",y)

print("10,2 array",z)
