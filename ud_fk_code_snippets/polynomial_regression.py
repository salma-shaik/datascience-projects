import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

np.random.seed(2)
pageSpeeds = np.random.normal(3, 1, 1000)
purchaseAmount = np.random.normal(50, 10, 1000)/pageSpeeds

# plt.scatter(pageSpeeds, purchaseAmount)
# plt.show()


# fit a 4th degree polynomial
x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

p4 = np.poly1d(np.polyfit(x, y, 8))

xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')

# plt.plot(x, p4(x), c='g')
plt.show()

r2 = r2_score(y, p4(x))
print(r2)
# print(r21)

# plt.scatter(pageSpeeds, purchaseAmount)
# plt.scatter(pageSpeeds, fitLine)
# # plt.plot(pageSpeeds, fitLine, c='r')