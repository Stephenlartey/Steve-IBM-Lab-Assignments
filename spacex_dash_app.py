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
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(data, values='class', 
        names='pie chart names', 
        title='title')
        return fig
    else:
        # return the outcomes piechart for a selected site
dcc.RangeSlider(id='payload-slider',
                min=0, max=10000, step=1000,
                marks={0: '0',
                       100: '100'},
                value=[min_payload, max_payload])
@app.callback([Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value')],
               Output(component_id='success-payload-scatter-chart', component_property='figure'))

def get_scatter_plot(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.scatter(data, values='class', 
        names='scatter plot names',
        color='Booster Version Category' 
        title='title')
        return fig
    else:
        return the outcomes scatter plot for a selected site

# Run the app
if __name__ == '__main__':
    app.run_server()
