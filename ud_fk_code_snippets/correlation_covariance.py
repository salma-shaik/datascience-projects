import numpy as np

pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000)

print(np.cov(pageSpeeds, purchaseAmount))
print(np.corrcoef(pageSpeeds, purchaseAmount))
