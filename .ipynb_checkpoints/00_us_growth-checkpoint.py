import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('C:/Users/Jmen3/Desktop/Programs/Python/Economic Growth/')

growth_data = pd.read_csv('data/growth.csv')
us_data = growth_data[growth_data['location_code']=="USA"]
us_data = us_data.drop_duplicates(subset=['year'])
us_data['gdp_lag'] = us_data['rgdpe'].shift(1)
us_data['growth'] = 100 * (((us_data['rgdpe'])-(us_data['gdp_lag']))/(us_data['gdp_lag']))

us_data.plot(x = 'year', y = 'growth')
plt.show()