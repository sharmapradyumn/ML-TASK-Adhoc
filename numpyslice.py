#!/usr/bin/python3

import numpy as np

a = np.array([(1,2,3,4),(5,6,7,80),(1,4,8,12)])

# print the 4th column

print(a[0:,3]) # 0:----> all rows  and only 3rd column

# print only 80

print(a[1,3]) # 1---> its 2nd row and 4th column

# print 3 and 12

print(a[0,2])# 0 row and 2 column

print(a[:,:-1]) # all row and exclude the last column

print(a[:,-1]) # all row and only last column

print(a[-2:]) # its print -2 and -1 row

# split concept

split = 2

print(a[:split,split]i) # its assign 2 to split 

print(a)
