import pandas as pd
import numpy as np
import chart_studio.plotly as py
import seaborn as sns
import yfinance as yf
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px

#tool to pull data from google finance and look at stock values being charted.

today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=1000)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

googlestock = yf.download('GOOG',
                          start=start_date,
                          end=end_date,
                          progress=False)

amdstock = yf.download('AMD',
                      start=start_date,
                      end=end_date,
                      progress=False)

googlestock["Date"] = googlestock.index
googlestock = googlestock[["Date", "Open", "High", "Low",
             "Close", "Adj Close", "Volume"]]
googlestock.reset_index(drop=True, inplace=True)

amdstock["Date"] = amdstock.index
amdstock = amdstock[["Date", "Open", "High", "Low",
             "Close", "Adj Close", "Volume"]]
amdstock.reset_index(drop=True, inplace=True)

print(googlestock.head())
print(amdstock.head())

figure = go.Figure(data=[go.Candlestick(x=googlestock['Date'],
                                        open=googlestock['Open'], high=googlestock['High'],
                                        low=googlestock['Low'], close=googlestock['Close'])])
figure.update_layout(title='Google Stock Price Analysis', xaxis_rangeslider_visible=False)

figure2 = px.line(googlestock, x='Date', y='Close',
                  title='Stock Market Analysis with Time Period Selectors')

figure2.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

figure3 = px.line(amdstock, x='Date', y='Close',
                  title='Stock Market Analysis with Time Period Selectors')

figure3.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)


figure.show()

figure2.show()

figure3.show()