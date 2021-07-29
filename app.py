import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

url = 'https://github.com/talverdi/flying-dog-beers/blob/master/student-por.csv'

df = pd.read_csv(url,sep=",")





# ########### Define your variables
# beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
# ibu_values=[35, 60, 85, 75]
# abv_values=[5.4, 7.1, 9.2, 4.3]
# color1='darkgreen'
# color2='orange'
# mytitle='Beer Comparison'
# tabtitle='beer!'
# myheading='Flying Dog Beers'
# label1='IBU'
# label2='ABV'
# githublink='https://github.com/austinlasseter/flying-dog-beers'
# sourceurl='https://www.flyingdog.com/beers/'

# ########### Set up the chart
# bitterness = go.Bar(
#     x=beers,
#     y=ibu_values,
#     name=label1,
#     marker={'color':color1}
# )
# alcohol = go.Bar(
#     x=beers,
#     y=abv_values,
#     name=label2,
#     marker={'color':color2}
# )

# beer_data = [bitterness, alcohol]
# beer_layout = go.Layout(
#     barmode='group',
#     title = mytitle
# )

# beer_fig = go.Figure(data=beer_data, layout=beer_layout)
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

app.layout = html.Div(children=[
    html.H4(children='Student Performance Table'),
    dcc.Dropdown(id='dropdown', options=[
        {'label': i, 'value': i} for i in df.Fjob.unique()
    ], multi=True, placeholder='Filter by Father Education...'),
    html.Div(id='table-container')
])

@app.callback(
    dash.dependencies.Output('table-container', 'children'),
    [dash.dependencies.Input('dropdown', 'value')])
def display_table(dropdown_value):
    if dropdown_value is None:
        return generate_table(df)

    dff = df[df.Fjob.str.contains('|'.join(dropdown_value))]
    return generate_table(dff)

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})




# ########### Initiate the app
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# server = app.server
# app.title=tabtitle

# ########### Set up the layout
# app.layout = html.Div(children=[
#     html.H1(myheading),
#     dcc.Graph(
#         id='flyingdog',
#         figure=beer_fig
#     ),
#     html.A('Code on Github', href=githublink),
#     html.Br(),
#     html.A('Data Source', href=sourceurl),
#     ]
# )

if __name__ == '__main__':
    app.run_server()
