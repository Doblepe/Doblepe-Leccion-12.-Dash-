
from jupyter_dash import JupyterDash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import matplotlib.pyplot as plt
import yfinance as yf
 
#Creamos una lista con los tickers a descargar
lista_precios = ['TSLA', 'GOOG', ]
#Descargamos todos los tickers de la lista y sólo los datos que necesitamos
precios = yf.download(lista_precios, start="2012-01-01")['Adj Close']

 
#Mostramos los cinco primeros registros del resultado para depurar
#print(precios.head(5))
 
#Dibujamos una gráfica con el resultado
plt.figure(figsize=(10,7))
#Preparamos cada ticker
precios['GOOG'].plot()
precios['TSLA'].plot()
#Configurarmos la gráfica
plt.title('Precios Google y Tesla', fontsize=14)
plt.xlabel('Año-Mes', fontsize=12)
plt.ylabel('Precio', fontsize=12)
#Mostramos la leyenda para saber qué color corresponde a cada empresa
plt.legend()
#Mostramos la gráfica
#plt.show()

figura = px.line(precios,title="Cotización de TESLA y Google de enero del 2015 a diciembre del 2018")
app = JupyterDash(__name__)
app.layout = html.Div(children=[
    html.H1(children="APLICACIÓN CON DASH PARA MERCADOS FINANCIEROS"),
    dcc.Graph(figure=figura)
])
if __name__ == "__main__":
    app.run_server(mode="inline")