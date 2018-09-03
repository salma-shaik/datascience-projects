import numpy as np
import matplotlib.pyplot as plt
# import statsmodels.
from sklearn.metrics import r2_score

np.random.seed(2)

pageSpeeds = np.random.normal(3, 1, 100)
purchaseAmount = np.random.normal(50, 30, 100)/pageSpeeds
# plt.scatter(pageSpeeds, purchaseAmount)
# plt.show()


# get train and test data
train_pageSpeeds = pageSpeeds[:80]
test_pageSpeeds = pageSpeeds[80:]

train_purchaseAmount = purchaseAmount[:80]
test_purchaseAmount = purchaseAmount[80:]

train_pageSpeeds_arr = np.array(train_pageSpeeds)
train_purchaseAmount_arr = np.array(train_purchaseAmount)

# plt.scatter(train_pageSpeeds, train_purchaseAmount)
# plt.show()

# plt.scatter(test_pageSpeeds, test_purchaseAmount)
# plt.show()

# fitting a 8th order polynomial using the training data
fitted_poly = np.poly1d(np.polyfit(train_pageSpeeds_arr, train_purchaseAmount_arr, 9))
# fitted_poly helps to predict new data

# plot the polynomial against the train data
xp =np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0, 7])
axes.set_ylim([0, 200])
# plt.scatter(train_pageSpeeds_arr, train_purchaseAmount_arr)
# plt.plot(xp, fitted_poly(xp), c='r')
# plt.show()

# plot the polynomial against the test data
test_pageSpeeds_arr = np.array(test_pageSpeeds)
test_purchaseAmount_arr = np.array(test_purchaseAmount)
plt.scatter(test_pageSpeeds_arr, test_purchaseAmount_arr)
plt.plot(xp, fitted_poly(xp), c='r')
# plt.show()

r2_train = r2_score(train_purchaseAmount, fitted_poly(train_pageSpeeds))
print('r2_train: ', r2_train)

r2_test = r2_score(test_purchaseAmount, fitted_poly(test_pageSpeeds))
print('r2_test: ', r2_test)

