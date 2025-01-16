# utils/stock_data.py
import yfinance as yf
import pandas as pd

# Função para obter os dados da ação
def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period='1d', interval='1m')
        if data.empty:
            raise ValueError(f"Nenhum dado encontrado para o ticker: {ticker}.")
        return data
    except Exception as e:
        print(f"Erro ao obter dados para {ticker}: {e}")
        return pd.DataFrame()
