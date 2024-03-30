import streamlit as st
import plotly.express as px
import sqlite3
import time

connection = sqlite3.connect("data.db")

plot = st.empty()

while True:
    cursor = connection.cursor()
    cursor.execute("Select date,time,temp from temperatures")
    rows = cursor.fetchall()
    print(rows)

    dates = []
    temps = []
    for row in rows:
        dates.append(f"{row[0]}-{row[1]}")
        temps.append(row[2])

    figure = px.line(x=dates, y=temps,
                    labels={"x":"Date", "y": "Temperature (C)"})

    plot.plotly_chart(figure, update="new")
    time.sleep(1)