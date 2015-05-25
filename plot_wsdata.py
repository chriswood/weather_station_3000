#!/usr/bin/python

import plotly.plotly as py
from plotly.graph_objs import *
from datetime import datetime
import sqlite3
import sys

db = '/home/pi/library/weather.db'

conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
conn.row_factory = sqlite3.Row
c = conn.cursor()

query = """SELECT date as "[timestamp]",  pressure as p,
                  temp as tbmp, humidity as h, dht_temp as tdht
           FROM measurements"""
#(datetime.datetime(2015, 5, 24, 0, 19, 39), u'102075', u'75.56', u'38.0', u'75.2')
c.execute(query)
res = c.fetchall()
axis1 = [r[0] for r in res]

trace1 = Scatter(
    x = axis1,
    y = [((float(r['p']) - 101000.0) / 10.0) for r in res],
    name = 'Pressure 1/10 (Pascal - 101000)',
    mode = 'lines+markers'
)
trace2 = Scatter(
    x = axis1,
    y = [r['h'] for r in res],
    name = 'humidity (%)',
    mode = 'lines+markers'
)
trace3 = Scatter(
    x = axis1,
    y = [r['tbmp'] for r in res],
    name = "Temp (F)",
    mode = 'lines+markers'
)
data = Data([trace1, trace2, trace3])
plot_url = py.plot(data, filename='weather_data')
print(plot_url)

