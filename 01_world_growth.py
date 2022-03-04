import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('C:/Users/Jmen3/Desktop/Programs/Python/Economic Growth/')

growth_data = pd.read_csv('data/macro_data.csv')
growth_data = growth_data.drop_duplicates(subset=['year','location_code'])
growth_data['gdp_lag'] = growth_data.groupby('location_code')['rgdpe'].shift(1)
growth_data['growth'] = 100 * (((growth_data['rgdpe'])-(growth_data['gdp_lag']))/(growth_data['gdp_lag']))

us_data = growth_data[growth_data['location_code']=="USA"]

us_data.plot(x = 'year', y = 'growth')
plt.show()

growth_data.to_csv('data/growth.csv', index=False)