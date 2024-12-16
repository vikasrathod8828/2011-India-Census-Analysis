import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

ecss=[
    {
"href":"https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",
"rel":"stylesheet",
"integrity":"sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC",
"crossorigin":"anonymous"}
]
df=pd.read_csv("india.csv")

state_list=[{"label":"India","value":"India"}]
for i in df["State"].unique():
    state_list.append({"label":i,"value":i})

primary= secondary=[]
for i in df.columns[4:]:
    primary.append({"label":i,"value":i})


app = dash.Dash(__name__,external_stylesheets=ecss)
app.layout=html.Div([
    html.H1("✯ 2011 India Census Analysis ✯",className="text-info text-center mt-5",style={'backgroundColor':'white'}),
    html.Div([
        html.Div([
            dcc.Dropdown(id="state",options=state_list,value="India")
        ],className="col-md-4 mt-5"),
        html.Div([
        dcc.Dropdown(id="primary",options=primary,value=primary[0]["value"])
        ],className="col-md-4 mt-5"),
        html.Div([
        dcc.Dropdown(id="secondary",options=secondary,value=secondary[0]["value"])
        ],className="col-md-4 mt-5"),
    ],className="row"),
    html.Div([
        dcc.Graph(id="Map")
    ],className="row mt-5"),
],className="container")



@app.callback(Output("Map","figure"),
              [Input("state","value"),
               Input("primary","value"),
               Input("secondary","value")])
def update(choice1,choice2,choice3):
    if choice1 == "India":
        return px.scatter_mapbox(df, lat="Latitude", lon="Longitude",
                  mapbox_style="carto-positron",zoom=5.5,height=650,hover_name="District",size_max=25,size=choice2,color=choice3)
    else:
        return px.scatter_mapbox(df[df["State"]== choice1], lat="Latitude", lon="Longitude",
                                 mapbox_style="carto-positron", zoom=3.5,hover_name="District", height=650, size_max=50,size=choice2, color=choice3)
app.run_server(debug=True)



