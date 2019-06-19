#!/usr/bin/python3

import matplotlib.pyplot as pl
# only loading python ori lib
x=[2,3]
y=[9,5]
pl.xlabel("time")
pl.ylabel("speed")
pl.plot(x,y,label="water")# this will draw a straight line
pl.bar(x,y)
pl.grid(color='green')
pl.legend() #to show the lable with plot
pl.xlim(0,12)#to show min to max in graph
pl.ylim(0,15)
pl.show()
