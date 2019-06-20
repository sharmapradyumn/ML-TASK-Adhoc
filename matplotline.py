#!/usr/bin/python3
#  from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

players=['MSD','virat','Sharma','Pandya']# its work as x
matches=[1,5,6,8]# differnet line
runs=[200,300,400,100] # as a y

plt.plot(players,runs)

plt.plot(matches)

plt.title("players run using Line graphs")

plt.xlabel("Players")
plt.ylabel("runs")

plt.show()

