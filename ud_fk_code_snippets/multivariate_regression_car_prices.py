import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

cars_info = pd.read_excel('data_files/cars.xls')

# sneak peak of the data - top 5 rows
# print(cars_info.head())

mil_cyl_doors = cars_info[['Mileage', 'Cylinder', 'Doors']]
price = cars_info['Price']

scale = StandardScaler()
mil_cyl_doors[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(mil_cyl_doors[['Mileage', 'Cylinder', 'Doors']].values)

# print(mil_cyl_doors)

# Ordinary Least Squares Fit
ols_est = sm.OLS(price, mil_cyl_doors).fit()
print(ols_est.summary())

# Mean price for 2 and 4 door cars
print(price.groupby(cars_info.Doors).mean())

