# Imports
import dash
from dash.dependencies import Input,Output
from dash import html,dcc
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from utils import temp_thresh,hum_thresh
from collections import deque
from datetime import datetime
import random
#from sensor import medicion

# Define una aplicación de flask, aloja la app de Dash
app = dash.Dash(__name__)
app.title = "Cuida a tu poroto 🫘"

# Intervalos de tiempo, temperatura y humedad
t =  deque(maxlen=50)
Temp = deque(maxlen=50)
Hum = deque(maxlen=50) 
t.append(datetime.now())

colors = {'background':'#274e3d','text':'#c0f1a3'}
# Diseño de la aplicación de Dash
app.layout = html.Div(style={'margin':0,'padding':0 ,'width':'100%', 'height':'100vh','overflow':'hidden',
                             'backgroundColor':colors['background']}
                             ,children=[html.H1(children="Estado de salud de tu poroto", 
                                                style={'textAlign':'center','color':colors['text'],
                                                       'font-family':'Arial'}),
                      dcc.Graph(id='live-graph',animate=True),
                      dcc.Interval(id='graph-update',interval=5000,n_intervals=0),
                      html.Div(id='alert-msg1'),
                      html.Div(id='alert-msg2')  
                    ])
def dummy_med():
    med1 = random.uniform(10,40)
    med2 = random.uniform(10,40)
    return med1,med2

m1,m2 = dummy_med()
Temp.append(m1)
Hum.append(m2)



@app.callback([Output('live-graph','figure'),Output('alert-msg1','children'),Output('alert-msg2','children')],
              [Input('graph-update','n_intervals')])

def update_graph_scatter(n):
    m1,m2 = dummy_med()
    t.append(datetime.now())
    Temp.append(m1)
    Hum.append(m2)
    data1 = go.Scatter(
		x = list(t),
		y = list(Temp),
		name = 'Temperatura [°C]',
		mode = 'lines+markers',
        line = dict(color="#52489c")
	)

    data2 = go.Scatter(
		x = list(t),
		y = list(Hum),
		name = 'Humedad [%]',
		mode = 'lines+markers',
        line = dict(color="#f14167")
	)

    fig = go.Figure(data=[data1, data2])
    fig.update_layout(title={'text':"Temperatura y Humedad en tiempo real",'x':0.5,'y':0.9,'xanchor':'center','yanchor':'top'},
		xaxis = dict(range = [min(t), max(t)]),
		yaxis = dict(range = [min(min(Temp), min(Hum)), max(max(Temp), max(Hum))]),
        paper_bgcolor = colors['background'],
        font = {'color':colors['text']},
        autosize=False,
        width=1300,
        height=400
	)
    fig.update_yaxes(automargin=True)
    m1 = round(m1,2)
    m2 = round(m2,2)
    msg1 = temp_thresh(m1)
    msg2 = hum_thresh(m2)
    return fig,html.P(msg1,style={'color':colors['text'],'textAlign':'center','font-family':'Arial'}),html.P(msg2,style={'color':colors['text'],'textAlign':'center','font-family':'Arial'})

# Corre el servidor
if __name__ == '__main__':
    app.run_server()