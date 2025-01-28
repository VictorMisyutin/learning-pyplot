import matplotlib.pyplot as plt
import numpy as np

# can make a graphic with multiple plots using plt.subplot
x = np.array([1,5,8,5,8])
y = np.array([3,5,6,8,7])

plt.subplot(2,1,1) # the diagram will have 1 row with 2 columns and I am doing the first plot right now
plt.plot(x,y, '*--g', mfc='#FF0000', mec="#00FF00", lw=5, ms= 20)
plt.title("Y grid only", loc='left')
plt.xlabel("First X Axis")
plt.ylabel("First Y Axis")
plt.grid(axis='y', color='#0000FF')

x = np.array([3,6,2,7,8])
y = np.array([1,2,5,7,8])

plt.subplot(2,1,2) # the diagram will have 1 row with 2 colums and I am doing the second plot right now
plt.plot(x,y)
plt.title("X grid only", loc='right')
plt.xlabel("Second X Axis")
plt.ylabel("Second Y Axis")
plt.grid(axis='x', color='#AA6600')

plt.suptitle("Trying Multple Graphs") # super title shows as tiltle for whole diagram not just one plot
plt.show()