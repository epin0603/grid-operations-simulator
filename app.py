#Plot the synthetic data and the simulated data in an interactive, web-based app

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

#Load the data
data_original = pd.read_csv('grid_data.csv')
data_simulated = pd.read_csv('simulation_results.csv')

#Convert 'Time' column to datetime format
data_original['Time'] = pd.to_datetime(data_original['Time'])
data_simulated['Time'] = pd.to_datetime(data_simulated['Time'])

app = dash.Dash(__name__)

#Initializing figures
first_figure = {}
simulation_figure = {}

#Layout of the app
app.layout = html.Div([
    html.H1("Grid Operations Simulation"), #Main title, change as needed
    dcc.Graph(id='original-graph', figure=first_figure),
    html.Div(style={'height': '50px'}),
    dcc.Graph(id='simulation-graph', figure=simulation_figure),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,
        n_intervals=0
    )
])

#Callback to update the original graph
@app.callback(
    Output('original-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_original_graph(n):
    original_data = data_original.iloc[:n+1]
    updated_figure = {
        'data': [
            {'x': original_data['Time'], 'y': original_data['Demand'], 'type': 'line', 'name': 'Demand'},
            {'x': original_data['Time'], 'y': original_data['SolarGeneration'], 'type': 'line', 'name': 'Solar Generation'},
            {'x': original_data['Time'], 'y': original_data['WindGeneration'], 'type': 'line', 'name': 'Wind Generation'},
        ],
        'layout': {
            'title': 'Grid Operations - Original Data'
        }
    }
    return updated_figure

#Callback to update the simulation graph
@app.callback(
    Output('simulation-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_simulation_graph(n):
    simulated_data = data_simulated.iloc[:n+1]
    updated_figure = {
        'data': [
            {'x': simulated_data['Time'], 'y': simulated_data['Demand'], 'type': 'line', 'name': 'Demand'},
            {'x': simulated_data['Time'], 'y': simulated_data['SolarGeneration'], 'type': 'line', 'name': 'Solar Generation'},
            {'x': simulated_data['Time'], 'y': simulated_data['WindGeneration'], 'type': 'line', 'name': 'Wind Generation'},
        ],
        'layout': {
            'title': 'Grid Operations - Simulated Data'
        }
    }
    return updated_figure

if __name__ == '__main__':
    app.run_server(debug=True)
