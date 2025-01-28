import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8, 15, 20])
ypoints = np.array([3, 10, 11, 17])

plt.plot(xpoints, ypoints, 'o--r', ms=15) # plot x and y points.

#'o' parameter stands for rings and does not draw line from point to point
# marker = '*' changes what the coordinate point looks like
# shorthand for changing the line is "MarkerLineColor" such as "o:r" which draws ring markers with a dotted like in red
# ms changes marker size (i think default is 6)
# mfc changes the color of the marker face (can use default color or hex)
# mef chanes the color of the marker edge (can use default color or hex)
# linewidth or lw changes the line width


plt.title("My super cool title", loc='left')
# loc changes the location of the title

# can change the font details of the labels using a font dictionary
font1 = {'family': 'serif', 'color': 'red', 'size': 10}
font2 = {'family': 'sans', 'color': 'blue', 'size': 10}

plt.xlabel("My X Label", font1)
plt.ylabel("My Y Label", font2)

# can display grid on plot
plt.grid()
# if you want grid lines on just one axis and do axis='y' or 'x'
# color changes color
# linestyle can change dashed, dotted, or solid
# linewidth changes the line width

plt.show()