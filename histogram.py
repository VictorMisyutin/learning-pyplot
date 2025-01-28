import matplotlib.pyplot as plt
import numpy as np

# histograms produce a graph that shows the frequencies of values

# making sample values
x = np.random.normal(170, 10, 250) # generate 250 values around 170 with standard deviation of 10

# takes one value param which is an array of values
plt.hist(x)
plt.show()

# can still use all other stuff like labels, color, height, whatever