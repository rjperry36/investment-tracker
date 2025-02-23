import streamlit as st
import pandas as pd
import yfinance as yf

# Web App Title
st.title("📈 AI Investment Tracker")
st.write("Live Market Updates & AI Alerts")

# Define stocks & ETFs to track
stocks = ["AAPL", "NVDA", "MSFT", "GOOGL", "XOM", "BP", "NEE", "SPY", "VEA", "SCHD"]

# Function to fetch real-time stock prices
def fetch_stock_data():
    data = yf.download(stocks, period="1d", interval="1h")["Close"]
    return data.iloc[-1]

# Show live stock prices
stock_prices = fetch_stock_data()
st.subheader("📊 Current Stock Prices")
st.table(stock_prices)

# Add a refresh button
if st.button("🔄 Refresh Data"):
    stock_prices = fetch_stock_data()
    st.table(stock_prices)

# Display AI-driven buy/sell alerts (placeholder)
st.subheader("📢 AI Alerts (Coming Soon)")
st.write("AI-based stock predictions will be integrated in future updates.")

# Footer
st.write("© 2024 Investment Tracker | Designed for iPhone Users")
import streamlit as st

st.title("📈 Investment Tracker")
st.write("Hello Russell! Your web app is now working.")

