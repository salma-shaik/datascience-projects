import pandas as pd
import statsmodels.api as sm
from scipy import stats
from scipy.signal import savgol_filter
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

cars_info = pd.read_excel('data_files/cars.xls')

features = cars_info[['Liter', 'Cruise', 'Sound', 'Leather']]
# print(features.head())

price = cars_info['Price']
# print(price.head())

# # Check whether cruise has any effect on price
# print(price.groupby(cars_info.Cruise).mean()) # 1- highly priced than 0
#
# Check whether litre has any effect on price
# print(price.groupby(cars_info.Liter).mean()) # not obvious
#
# # Check whether sound has any effect on price
# print(price.groupby(cars_info.Sound).mean()) # not much of a difference
#
# # Check whether Leather has any effect on price
# print(price.groupby(cars_info.Leather).mean()) # Slight difference

# First, normalize the data for OLS Estimate
scale = StandardScaler()

features[['Liter', 'Cruise', 'Sound', 'Leather']] = scale.fit_transform(features[['Liter', 'Cruise', 'Sound', 'Leather']].values)

# print(features)

# Ordinary Least Squares Fit
features_est = sm.OLS(price, features).fit()
# print(features_est.summary())

# Doors vs Price
doors = cars_info['Doors']
slope, intercept, r_value, p_value, std_err = stats.linregress(doors, price)
# print(r_value ** 2)


# Predict price from doors
def predict_price(doors):
    return slope*doors + intercept


# print(predict_price(8))

# Litres vs Price
# price_litres = price.groupby(cars_info.Liter).mean()
# print(type(price_litres))
# plt.xlabel('Liter')
# plt.ylabel('Car Price')
# # plt.plot(price_litres)
# # plt.show()
#
# # To smooth out the curve
# plt.plot(price_litres.index, savgol_filter(price_litres.values, 7, 3))
# plt.show()


# Make vs Price
price_make = price.groupby(cars_info.Make).mean()
print(price_make)
# plt.bar(price_make)
# plt.show()

price_make_model = price.groupby([cars_info.Make, cars_info.Model]).mean()
print(price_make_model)
