import matplotlib.pyplot as plt
from pylab import randn
import numpy as np

rand_age = np.random.randint(3, 100, 100)
rand_time = np.random.randint(1, 24, 100)

# axes = plt.axes()

plt.xlabel('Age(years)')
plt.ylabel('Time Spent(hours)')

plt.scatter(rand_age, rand_time)

plt.show()