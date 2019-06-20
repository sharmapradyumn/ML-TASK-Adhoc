#!usr/bin/python3

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')  # its use for background

x=[2,4,6,8]

y=[8,10,23,14]

x1=[4,5,6,7]
y1=[8,91,34,45]

plt.plot(x,y,color='green',label='line1',linewidth='5') # line label

plt.plot(x1,y1,color='blue',label='line2',linewidth='5') # line label


plt.title("matplotlib style uses")

plt.xlabel("a-axis")
plt.ylabel("y-axis")

plt.legend() # its draw the small line on top of right side for label

plt.grid(True,color='red') # for background lines

plt.show()
