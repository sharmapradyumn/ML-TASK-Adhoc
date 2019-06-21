#!/usr/bin/python3

import matplotlib.pyplot as plt
import pandas as pd

p=pd.read_csv('studentdata.csv')#,header=None)
print(p)

plt.title("Student marks pie chart")

plt.pie(p.iloc[:,1],explode=(0.5,0,0,0.05),autopct='%.1f%%',labels=p.iloc[:,0],shadow=True) # iloc slice the perticular raw and column here pie chart for student marks
plt.show()

plt.title("Student age pie chart")

plt.pie(p.iloc[:,2],explode=(0.5,0,0,0.05),autopct='%.1f%%',labels=p.iloc[:,0],shadow=True)

plt.legend()# small lines for labels
plt.axis('equal')
plt.show()

