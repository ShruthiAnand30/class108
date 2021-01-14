import random
import plotly.express as px
import plotly.figure_factory as ff

dicelist = []
count = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dicelist.append(dice1 + dice2)
    count.append(i)

#fig = px.bar(x = dicelist, y = count)
fig = ff.create_distplot([dicelist], ["Result"])
fig.show()