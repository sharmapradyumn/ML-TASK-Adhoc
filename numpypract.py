#!/usr/bin/python3
import numpy as np
a = np.array([1,2,3])#syntax with []
b = np.array((1,24,5))#syntax with ()

c = np.array([[1,2,4],[5,6,7]])#2d array using []
d = np.array([(6,7,8),(9,5,6)])#2d array using ()

print(a.ndim)#ndim use for matrix dimenson
print(c.ndim)

print(a.itemsize)# itemsize is use for show the size of item
print(c.itemsize)

print(a.dtype)# dtype is use for check the type of data 
print(c.dtype)

print(a.size) #size is use for check the size of matrix or number of item in mtx
print(c.size)

print(a.shape) # check the shape of matrix ex.--->   4*3 or 3*4
print(c.shape)

print(a.reshape(3,1))  # reshape the matrix 
print(c.reshape(3,2))

print(np.linspace(1,7,6)) # its print the values between two numbers with a gap(n1,n2,how many numbers)

print(a.max())# its print max in the matrix
print(c.min())# min in matrix
print(c.sum())# its print sum of matrix numbers

print(d.sum(axis=1)) # its print the sum of rows
print(c.sum(axis=0)) # its print the sum of columns

print(np.hstack(c)) # its convert matrix in horizontal
print(np.vstack(a))

print(d.ravel) # print mtrix in column form 
print(a)
print(b)

print(c)
print(d)
