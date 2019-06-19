#!/usr/bin/python3

import matplotlib.pyplot as pl
# only loading python ori lib
player=["MS","VIRAT","pandya"]
runs=[250,300,150]
pl.xlabel("player")
pl.ylabel("runs")
#pl.plot(x,y,label="water")# this will draw a straight line
pl.bar(player,runs)
pl.grid(color='green')
pl.legend() #to show the lable with plot
#pl.xlim(0,12)#to show min to max in graph
#pl.ylim(0,15)
pl.show()
