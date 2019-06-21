#!/usr/bin/python3
import numpy as np

row=int(input("Enter number of rows"))
column=int(input("Enter number of columns"))

array2D= np.random.rand(row,column) # 
print("random numbers of 2D array is  :\n",array2D)

np.savetxt('array.txt',array2D)
np.loadtxt('array.txt')
