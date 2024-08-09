#This simple simulator focuses on dynamic load simulation by altering demand and generation.

import simpy
import pandas as pd
import numpy as np

class GridSimulator:
    def __init__(self, env, data):
        self.env = env
        self.data = data
        self.current_time_index = 0
        self.results = []

    def update(self):
        while self.current_time_index < len(self.data):
            #Simulating demand and generation with some randomness
            demand = self.data['Demand'].iloc[self.current_time_index] * (1 + np.random.normal(0, 0.05)) #Varies by ±5%. Change as needed
            solar_generation = self.data['SolarGeneration'].iloc[self.current_time_index] * (1 + np.random.normal(0, 0.1)) #Varies by ±10%. Change as needed
            wind_generation = self.data['WindGeneration'].iloc[self.current_time_index] * (1 + np.random.normal(0, 0.1)) #Varies by ±10%. Change as needed
            
            #Calculate net demand after variation changes
            net_demand = demand - (solar_generation + wind_generation)
            
            #Store the results
            self.results.append({
                'Time': self.data['Time'].iloc[self.current_time_index],
                'Demand': demand,
                'SolarGeneration': solar_generation,
                'WindGeneration': wind_generation,
                'NetDemand': net_demand
            })
            
            yield self.env.timeout(1)  #Advance the simulation by one hour
            self.current_time_index += 1

data = pd.read_csv('grid_data.csv')
data['Time'] = pd.to_datetime(data['Time'])

env = simpy.Environment()

grid_simulator = GridSimulator(env, data)

env.process(grid_simulator.update())
env.run()

results_df = pd.DataFrame(grid_simulator.results) #Dataframe created for the results of the simulation
results_df.to_csv('simulation_results.csv', index=False) #Change the name as needed
print("Simulation complete. Results saved to 'simulation_results.csv'.")
