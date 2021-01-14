import pandas as pa
import csv
import plotly.figure_factory as ff

df = pa.read_csv("data.csv")
fig = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height"], show_hist = False)
fig.show()