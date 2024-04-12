# Hands on Machine Learning with Python
import pandas
from sklearn.linear_model import LinearRegression
#import matplotlib.pyplot as plt
data = pandas.read_csv('iphone_price.csv')
#plt.barh(data['version'], data['price'])
#plt.show()
model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[20]]))
print(model.predict([[30]]))