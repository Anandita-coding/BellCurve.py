import random
import plotly.graph_objects as go
import plotly.figure_factory as ff

dice_result = []
count = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    dice_result.append(dice1+dice2)
    count.append(i)

fig = go.Figure(go.Bar(
    y = count,
    x = dice_result
))
fig.show()

fig1 = ff.create_distplot([dice_result],["Result"])
fig1.show()
