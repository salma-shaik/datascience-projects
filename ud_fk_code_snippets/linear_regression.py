import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score

pageSpeeds = np.random.normal(3, 1, 10)
print('pageSpeeds: ', pageSpeeds)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 10)) * 3
# print('purchaseAmount: ', purchaseAmount)
# plt.scatter(pageSpeeds, purchaseAmount)
# plt.show()

slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)

# linear regression
# print(r_value ** 2)
# print(intercept)


def predict(x):
    return slope * x + intercept


fitLine = predict(pageSpeeds)
print('fitLine: ', fitLine)

plt.scatter(pageSpeeds, purchaseAmount)
plt.scatter(pageSpeeds, fitLine)
# plt.plot(pageSpeeds, fitLine, c='r')
plt.xlabel('pageSpeeds')
plt.ylabel('purchaseAmount')
plt.show()

# print(r2_score(pageSpeeds, fitLine))