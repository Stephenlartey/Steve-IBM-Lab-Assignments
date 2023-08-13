# Import required libraries
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the spacex launch data into pandas dataframe
spacex_launch_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Create a dash application
app = dash.Dash(__name__)
# Application layout
# Adding a title to the dasdhboard
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard', 
                                style={'textAlign': 'center', 'color': '#503D36',
                                'font-size': 40}),

#### Pie Chart Creation
###fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')

dcc.Dropdown(id='id',
                options=[
                    {'label': 'All Sites', 'value': 'ALL'},
                    {'label': 'site1', 'value': 'site1'},
                ],
                value='ALL',
                placeholder="Select SpaceX launch site",
                searchable=True
                ),