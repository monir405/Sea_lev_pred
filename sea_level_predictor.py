import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = pd.read_csv('epa-sea-level.csv')
plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])
res = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
years_extended = pd.Series(range(1880, 2051))
plt.plot(years_extended, res.intercept + res.slope*years_extended, 'r')
new_data = data[data['Year'] >= 2000]
res_new = linregress(new_data['Year'], new_data['CSIRO Adjusted Sea Level'])
years_new = pd.Series(range(2000, 2051))
plt.plot(years_new, res_new.intercept + res_new.slope*years_new, 'g')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.show()
