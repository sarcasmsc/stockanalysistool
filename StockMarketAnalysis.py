import pandas as pd
import numpy as np
import chart_studio.plotly as py
import seaborn as sns
import yfinance as yf
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

#tool to pull data from yahoo finance and look at stock values being charted.

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

tslastock = yf.download('TSLA',
                      start=start_date,
                      end=end_date,
                      progress=False)

nvidiastock = yf.download('NVDA',
                      start=start_date,
                      end=end_date,
                      progress=False)

intelstock = yf.download('INTC',
                      start=start_date,
                      end=end_date,
                      progress=False)

amazonstock = yf.download('AMZN',
                      start=start_date,
                      end=end_date,
                      progress=False)

netflixstock = yf.download('NFLX',
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

tslastock["Date"] = tslastock.index
tslastock = tslastock[["Date", "Open", "High", "Low",
             "Close", "Adj Close", "Volume"]]
tslastock.reset_index(drop=True, inplace=True)

nvidiastock["Date"] = nvidiastock.index
nvidiastock = nvidiastock[["Date", "Open", "High", "Low",
             "Close", "Adj Close", "Volume"]]
nvidiastock.reset_index(drop=True, inplace=True)

intelstock["Date"] = intelstock.index
intelstock = intelstock[["Date", "Open", "High", "Low",
             "Close", "Adj Close", "Volume"]]
intelstock.reset_index(drop=True, inplace=True)

amazonstock["Date"] = amazonstock.index
amazonstock = amazonstock[["Date", "Open", "High", "Low",
             "Close", "Adj Close", "Volume"]]
amazonstock.reset_index(drop=True, inplace=True)

netflixstock["Date"] = netflixstock.index
netflixstock = netflixstock[["Date", "Open", "High", "Low",
             "Close", "Adj Close", "Volume"]]
netflixstock.reset_index(drop=True, inplace=True)

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

figure4 = px.line(tslastock, x='Date', y='Close',
                  title='Stock Market Analysis with Time Period Selectors')

figure4.update_xaxes(
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

figure5 = px.line(nvidiastock, x='Date', y='Close',
                  title='Stock Market Analysis with Time Period Selectors')

figure5.update_xaxes(
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

figure6 = px.line(intelstock, x='Date', y='Close',
                  title='Stock Market Analysis with Time Period Selectors')

figure6.update_xaxes(
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

figure7 = px.line(amazonstock, x='Date', y='Close',
                  title='Stock Market Analysis with Time Period Selectors')

figure7.update_xaxes(
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

figure8 = px.line(netflixstock, x='Date', y='Close',
                  title='Stock Market Analysis with Time Period Selectors')

figure8.update_xaxes(
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



def choice():
    print(""""Which stock would you like to look at?
            Choices:
            Google
            AMD
            Tesla
            Nvidia
            Intel
            Amazon
            Netflix""")

    stockchoice = input(" ").lower()

    if stockchoice == 'google':
        figure.show()
        figure2.show()
    elif stockchoice == 'amd':
        figure3.show()
    elif stockchoice == 'tsla':
        figure4.show()
    elif stockchoice == 'nvidia':
        figure5.show()
    elif stockchoice == 'intel':
        figure6.show()
    elif stockchoice == 'amazon':
        figure7.show()
    elif stockchoice == 'netflix':
        figure8.show()
    else:
        print('something went wrong')


def search():
    stockchoice = ticker_entry.get()
    if stockchoice == 'google':
        figure.show()
        figure2.show()
    elif stockchoice == 'amd':
        figure3.show()
    elif stockchoice == 'tesla':
        figure4.show()
    elif stockchoice == 'nvidia':
        figure5.show()
    elif stockchoice == 'intel':
        figure6.show()
    elif stockchoice == 'amazon':
        figure7.show()
    elif stockchoice == 'netflix':
        figure8.show()
    else:
        print('something went wrong')

# Create the main window
window = tk.Tk()
window.title("Stock Searcher")
window.geometry("200x150")

# Create the ticker entry field
ticker_entry = tk.Entry(window, width=200)
ticker_entry.pack()

# Create the search button
search_button = tk.Button(window, text="Search", command=search)
search_button.pack()

# Create the results label
results_label = tk.Label(window, text="")
results_label.pack()

# Run the main loop
window.mainloop()
