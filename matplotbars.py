#!/usr/bin/python3

import matplotlib.pyplot as plt

boys =[1,2,3,4]
gf=[2,3,10,8]

b=[12,34,56,14]
g=[6,20,40,10]

plt.bar(boys,gf,color='green',label='boys vs gf',)

plt.bar(b,g,color='blue',label='boys vs girls',)

plt.xlabel("boii")
plt.ylabel("girll")
plt.grid(True,color='black')
plt.legend()


plt.show()

