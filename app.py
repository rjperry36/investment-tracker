import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
import json
import os

# Web App Title
st.title("📈 AI Investment Tracker")
st.write("Live Market Updates & AI-Driven Investment Insights")

# Define Persistent Storage File
INVESTMENTS_FILE = "investments.json"

def load_investments():
    if os.path.exists(INVESTMENTS_FILE):
        with open(INVESTMENTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_investments(investments):
    with open(INVESTMENTS_FILE, "w") as file:
        json.dump(investments, file)

# Load Investments from File
if "investments" not in st.session_state:
    st.session_state["investments"] = load_investments()

# Function to Fetch Real-Time Stock Prices
def fetch_stock_data(tickers):
    if tickers:
        try:
            data = yf.download(tickers, period="1d", interval="1h")
            if data.empty:
                st.warning("No stock data retrieved. Please check ticker symbols.")
                return {}
            return data["Close"].iloc[-1]
        except Exception as e:
            st.error(f"Error retrieving stock data: {e}")
            return {}
    return {}

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

if st.sidebar.button("Add Investment", key="add_investment_button"):
    if ticker and investment_amount > 0:
        new_investment = {
            "Ticker": ticker.upper(),
            "Date": str(investment_date),
            "Time": str(investment_time),
            "Amount Invested (£)": investment_amount,
            "Fees (£)": investment_fees
        }
        st.session_state["investments"].append(new_investment)
        save_investments(st.session_state["investments"])
        st.sidebar.success(f"Added {ticker.upper()} investment on {investment_date}")
    else:
        st.sidebar.error("Please enter a valid ticker and investment amount.")

# Display Current Investments
st.subheader("📊 Your Investment Portfolio")
if st.session_state["investments"]:
    investment_df = pd.DataFrame(st.session_state["investments"])
    tickers = investment_df["Ticker"].unique()
    stock_prices = fetch_stock_data(tickers)
    if stock_prices:
        investment_df["Current Price (£)"] = investment_df["Ticker"].map(stock_prices.to_dict())
        investment_df["Profit/Loss (£)"] = investment_df["Current Price (£)"] - investment_df["Amount Invested (£)"]
        investment_df["Change (%)"] = (investment_df["Profit/Loss (£)"] / investment_df["Amount Invested (£)"]) * 100
    
        # Improved Table UI
        def highlight_changes(val):
            if val > 0:
                return "background-color: #ccffcc;"  # Green for positive changes
            elif val < 0:
                return "background-color: #ffcccc;"  # Red for negative changes
            else:
                return "background-color: #ffffcc;"  # Yellow for neutral values
    
        st.dataframe(investment_df.style.applymap(highlight_changes, subset=["Profit/Loss (£)", "Change (%)"]))
    else:
        st.warning("Could not retrieve stock data. Please check ticker symbols.")
else:
    st.info("No investments added yet. Use the sidebar to add investments.")

# Display AI Model Summaries
st.subheader("🧠 AI Model Insights")
ai_summary = analyze_models()
for model, summary in ai_summary.items():
    st.markdown(f"**{model}**: {summary}")

# Unique Key for Refresh Button to Avoid Duplicate Element Error
if st.button("🔄 Refresh Data", key="refresh_button_1"):
    if "last_refresh" not in st.session_state or (datetime.datetime.now() - st.session_state["last_refresh"]).seconds > 2:
        st.session_state["last_refresh"] = datetime.datetime.now()
        st.rerun()

# Footer
import subprocess

try:
    version = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode("utf-8").strip()
except:
    version = "Unknown"

st.write(f"RES Version {version}")
