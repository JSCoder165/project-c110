import statistics
import plotly_express as px
import pandas as pd
import math
import random
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist= False)
fig.show()

population_mean = statistics.mean(data)
print("mean = ", population_mean)
population_standarddeviation = statistics.stdev(data)
print("Standard deviation = ", population_standarddeviation)

dataset = []
for i in range(0, 1000):
  random_index = random.randint(0, len(data))
  value = data[random_index]
  dataset.append(value)

mean = statistics.mean(dataset)
standarddeviation = statistics.stdev(dataset)

print("mean of 1000 values", mean)
print("standard dev of 1000 ")