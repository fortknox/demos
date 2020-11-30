import dash
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

server = app.server 

app.title = 'Demo App'

header = dbc.Card([
    dbc.Row([
        dbc.col([html.H5('OUR FIRST APP DEMO')], width=7),
        dbc.col([html.Img(src='./assets/logo.jpg', style={'width':'100px','height':'140px'})], width=5)
    ], style={'align-items':'center'})
])


#def make_layout():
 #   return ()

app.layout = make_layout


if __name__ == '__main__':
    app.run_server(debug=False, port=8057)