import pandas as pd
import plotly.figure_factory as ff
 
df = pd.read_csv("project_data.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()],["Ratings"], show_hist = False) 
fig.show()