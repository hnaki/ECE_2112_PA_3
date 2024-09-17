# %%
import pandas as pd

# %%
cars = pd.read_csv('cars.csv')
cars

# %%
output_cars = cars.iloc[:, 1::2]
output_cars.head()

# %%
cars.loc[cars['Model'] == 'Mazda RX4']

# %%
cars.loc[(cars['Model'] == 'Camaro Z28'), ['Model','cyl']]

# %%
car_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(car_models)][['Model','cyl', 'gear']]

# %%



