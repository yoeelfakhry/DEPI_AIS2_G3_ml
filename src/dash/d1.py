import pandas as pd
import plotly.express as px 
from dash import Dash , dcc , html , Input , Output

df = pd.read_csv("E:\\microsoft machine learning\\labs\\DEPI_AIS2_G3_ml\\src\\dash\\sales_data.csv")
app = Dash(__name__)
app.title = "Interactive Dashboard"
num_cols = df.select_dtypes(include='number').columns

app.layout = html.Div([html.H1("Interactive Dashbord pie chart") ,
                      html.Label("Select a value to show in the bar") ,
                      dcc.Dropdown(id='columns_Dropdown' , options = [{'label':col , 'value':col} for col in num_cols] ,value =num_cols[0]) , 
                      dcc.Graph(id = 'pie_chart') ,
                                    ])

@app.callback(Output('pie_chart' , 'figure') , Input('columns_Dropdown' , 'value'))
def update_pie(selected_col):
    grouped = df.groupby('Area')[selected_col].sum().reset_index()
    fig = px.pie(grouped ,  names='Area' , values = selected_col , title= f"Distribution of {selected_col} by area"
                 , hole = 0.4 , color_discrete_sequence= px.colors.qualitative.Set2)
    return fig



if __name__ == "__main__" :
    app.run(debug=True)