#This program plots the synthetic data and the simulated data using matplotlib

import pandas as pd
import matplotlib.pyplot as plt

data_original = pd.read_csv('grid_data.csv')
data_simulated = pd.read_csv('simulation_results.csv')

#'Time' column to datetime format
data_original['Time'] = pd.to_datetime(data_original['Time'])
data_simulated['Time'] = pd.to_datetime(data_simulated['Time'])

fig, (ax1, ax2) = plt.subplots(2)

#Plot for original data
ax1.set(xlabel = 'Time', ylabel = 'Power (MW)', title = "Original Data")
ax1.plot(data_original['Time'], data_original['Demand'], label='Demand')
ax1.plot(data_original['Time'], data_original['SolarGeneration'], label='Solar Generation')
ax1.plot(data_original['Time'], data_original['WindGeneration'], label='Wind Generation')

#Plot for simulated data
ax2.set(xlabel = 'Time', ylabel = 'Power (MW)', title = "Simulated Data")
ax2.plot(data_simulated['Time'], data_simulated['Demand'], label='Demand')
ax2.plot(data_simulated['Time'], data_simulated['SolarGeneration'], label='Solar Generation')
ax2.plot(data_simulated['Time'], data_simulated['WindGeneration'], label='Wind Generation')

plt.legend()
plt.show()