
import streamlit as st
import yfinance as yf

st.set_page_config(page_title="תחזית זהב ומניות", layout="centered")
st.title("📊 תחזית חיה - מניות, זהב וקריפטו")

stocks = {
    'זהב (Plus500)': 'GC=F',
    'נאסד"ק (NASDAQ)': '^IXIC',
    'S&P 500': '^GSPC',
    'ביטקוין': 'BTC-USD',
    'אתריום': 'ETH-USD',
    'נאסד"ק 100': '^NDX',
    'ת"א 35': 'TA35.TA',
    'Nvidia': 'NVDA'
}

times = ['1 דקה', '5 דקות', '10 דקות', '30 דקות', 'שעה', 'יום', 'שבוע']

selected_stock = st.selectbox("בחר נכס", list(stocks.keys()))
selected_time = st.selectbox("בחר טווח זמן", times)
amount = st.number_input("סכום השקעה ($)", min_value=1, step=1, value=1000)

if st.button("קבל תחזית"):
    try:
        ticker = stocks[selected_stock]
        data = yf.download(ticker, period="1d", interval="1m")
        latest_price = data["Close"].dropna().iloc[-1]
        trend = "קנייה 🔼" if latest_price > data["Close"].mean() else "מכירה 🔽"
        percent = 1.5 if trend == "קנייה 🔼" else -1.2
        expected_return = amount * (1 + percent / 100)
        st.success(f"תחזית ל-{selected_stock} בטווח {selected_time}: {trend}")
        st.info(f"רווח/הפסד צפוי: ${expected_return - amount:.2f} (סה"כ: ${expected_return:.2f})")
    except Exception as e:
        st.error("אירעה שגיאה בעת טעינת הנתונים")
