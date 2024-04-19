import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
         # Simple web Applicaton
         
         Google stock prices
         
         """)

tickerSymbol = "GOOGL"

tickerData = yf.Ticker(tickerSymbol)

# print(tickerData)

tickerDf = tickerData.history(period="1d", start="2010-5-31", end="2020-5-31")

st.write("""## Closing Price""")

st.line_chart(tickerDf.Close)

st.write("""## Volume""")
st.line_chart(tickerDf.Volume)

st.write("""## Display Image""")
st.image("MainAfter.webp")

st.write("""# Just checking functions""")
st.error("This is error")

# markdown
st.markdown("# Intelligent")

# caption
st.caption("Captions are for instagram")

# mathematical expression

st.latex(r''' a+b x^2''')

# radio
st.radio("Pick your level", [1, 2, 3, 4])

# Select box
st.selectbox("Pick your course", ["ML", "MLOPS"])

# multiselect
st.multiselect("Choose the dept", ["Sales", "Marketing", "Accounting"])

# selectslider
st.select_slider("Rating", ["Bad", "Average", "Good", "Best"])

# slider
st.slider("Select number", min_value=0, max_value=100)

# number_input
st.number_input("This is number input", min_value=1, max_value=15, step=3)

#
