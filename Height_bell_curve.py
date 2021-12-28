import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv")

fig = ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist = False)
fig.show()

fig2 = ff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_curve = False)
fig2.show()