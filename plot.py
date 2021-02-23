import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


df = pd.read_csv('studentappdata.csv')
plot = go.Figure(go.Scatter(
    x = df.groupby('level')['attempt'].mean(),
    y = ['level 1', 'level 2', 'level 3', 'level 4'],
    mode='markers',
    marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3])
))

plot.show()


