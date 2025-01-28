import matplotlib.pyplot as plt
import numpy as np


xlabels = ['Apples', 'Bananas', 'Oranges', 'Kiwi']
yvalues = [134, 65, 86, 23]

plt.subplot(2,1,1)
# can draw bargraphs
plt.bar(xlabels, yvalues)
plt.title("Pounds of food sold in a day")

plt.subplot(2,1,2)
# can also make them horizontal
plt.barh(xlabels, yvalues)
plt.title("Pounds of food sold in a day")
plt.show()

#can also use paramters such as
# color: change color of each bar
# width: change width of each bar
# height: change percentage of value to make height
# etc: can google the rest
