import matplotlib.pyplot as plt
import numpy as np

values = [134, 65, 86, 23]

plt.subplot(2,2,1)
plt.pie(values)

labels = ['Apples', 'Bananas', 'Oranges', 'Kiwi']

plt.subplot(2,2,2)
plt.pie(values, labels=labels)
plt.title("Pie chart with labels")

plt.subplot(2,2,3)
explosion = [0.2,0,0,0]
plt.pie(values, labels=labels, explode=explosion)
plt.title("Pie chart with explosion")

plt.subplot(2,2,4)
mycolors= ['red', 'yellow', 'orange', 'green']
explosion = [0.3,0.1,0.1,0.1]

plt.pie(values, labels=labels, explode=explosion, shadow=True, colors=mycolors)
plt.legend(title="Fruits")
plt.title("Pie chart with other stuff")
plt.show()
# can also change starting angle (where first value is) using "startangle" paramter