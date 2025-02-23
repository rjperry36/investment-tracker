import streamlit as st
import pandas as pd
import yfinance as yf
import datetime

# Web App Title
st.title("📈 AI Investment Tracker")
st.write("Live Market Updates & AI-Driven Investment Insights")

# Define Session State for Storing Investments
if "investments" not in st.session_state:
    st.session_state["investments"] = []

# Function to Fetch Real-Time Stock Prices
def fetch_stock_data(tickers):
    data = yf.download(tickers, period="1d", interval="1h")["Close"]
    return data.iloc[-1]

# Function to Analyze AI Models (Russell, Sayjel, Ethan)
def analyze_models():
    summary = {
        "Russell": "📊 Russell suggests holding tech stocks as they show steady growth. Buy recommendation: AAPL, MSFT.",
        "Sayjel": "📉 Sayjel highlights volatility in energy stocks. Consider selling XOM and diversifying.",
        "Ethan": "⚡ Ethan detects short-term trading opportunities in ETFs. Recommended: SPY, VEA."
    }
    return summary

# Allow User to Add Investments
st.sidebar.header("📥 Add a New Investment")
ticker = st.sidebar.text_input("Enter Ticker Symbol (e.g., AAPL, TSLA)")
investment_amount = st.sidebar.number_input("Total Investment (£)", min_value=0.0, step=10.0)
investment_date = st.sidebar.date_input("Date of Investment", datetime.date.today())
investment_time = st.sidebar.time_input("Time of Investment", datetime.datetime.now().time())
investment_fees = st.sidebar.number_input("Investment Fees (£)", min_value=0.0, step=1.0)

if st.sidebar.button("Add Investment"):
    if ticker and investment_amount > 0:
        st.session_state["investments"].append({
            "Ticker": ticker.upper(),
            "Date": investment_date,
            "Time": investment_time,
            "Amount Invested (£)": investment_amount,
            "Fees (£)": investment_fees
        })
        st.sidebar.success(f"Added {ticker.upper()} investment on {investment_date}")
    else:
        st.sidebar.error("Please enter a valid ticker and investment amount.")

# Display Current Investments
st.subheader("📊 Your Investment Portfolio")
if st.session_state["investments"]:
    investment_df = pd.DataFrame(st.session_state["investments"])
    tickers = investment_df["Ticker"].unique()
    stock_prices = fetch_stock_data(tickers)
    investment_df["Current Price (£)"] = investment_df["Ticker"].map(stock_prices.to_dict())
    investment_df["Profit/Loss (£)"] = investment_df["Current Price (£)"] - investment_df["Amount Invested (£)"]
    investment_df["Change (%)"] = (investment_df["Profit/Loss (£)"] / investment_df["Amount Invested (£)"]) * 100
    
    # Improved Table UI
    def highlight_changes(val):
        return "background-color: #ffcccc;" if val < 0 else "background-color: #ccffcc;"
    
    st.dataframe(investment_df.style.applymap(highlight_changes, subset=["Profit/Loss (£)", "Change (%)"]))
else:
    st.info("No investments added yet. Use the sidebar to add investments.")

# Display AI Model Summaries
st.subheader("🧠 AI Model Insights")
ai_summary = analyze_models()
for model, summary in ai_summary.items():
    st.markdown(f"**{model}**: {summary}")

# Refresh Button
if st.button("🔄 Refresh Data"):
    st.experimental_rerun()

# Footer
st.write("© 2024 Investment Tracker | Designed for iPhone Users")
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

