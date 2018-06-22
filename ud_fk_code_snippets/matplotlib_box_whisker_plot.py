import matplotlib.pyplot as plt
import numpy as np

uniformSkewed = np.random.rand(100) * 100 - 40
high_outliers = np.random.rand(10) * 50 + 100
low_outliers = np.random.rand(10) * -50 - 100

data = np.concatenate((uniformSkewed, high_outliers, low_outliers))

plt.boxplot(data)
plt.show()

