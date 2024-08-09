#This synthetic data generator will output a csv file with time, demand, solar generation, and wind generation data produced with numpy's random module.

import pandas as pd
import numpy as np

np.random.seed(0) #Change the seed as needed
time = pd.date_range(start='2024-01-01', periods=100, freq='h') #Data is set hourly from Jan 1, 2024 to Jan 5. Change as needed
demand = np.random.normal(50, 10, size=len(time))
solar_generation = np.clip(np.random.normal(20, 5, size=len(time)), 0, None)
wind_generation = np.clip(np.random.normal(30, 7, size=len(time)), 0, None)

#Dataframe created using the synthetic data
data = pd.DataFrame({
    'Time': time,
    'Demand': demand,
    'SolarGeneration': solar_generation,
    'WindGeneration': wind_generation
})

#Creates csv file using the dataframe. Rename as needed
data.to_csv('grid_data.csv', index=False)