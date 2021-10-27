import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

#calculating the mean and standard deviation of the population data
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("mean of population: ",mean)
print("Standard deviation of population: ",std_deviation)

#function to find the mean of 100 data points 1000 times 
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,100):
    set_of_means= random_set_of_mean(30)
    mean_list.append(set_of_means)

stdev = statistics.stdev(mean_list)
sample_mean = statistics.mean(mean_list)

first_std_deviation_start, first_std_deviation_end =mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end =mean-(3*std_deviation), mean+(3*std_deviation)
print("standard deviation 1: ",first_std_deviation_start, first_std_deviation_end)
print("standard deviation 2: ",second_std_deviation_start, second_std_deviation_end)
print("standard deviation 3: ",third_std_deviation_start,third_std_deviation_end)

fig = ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.8], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.8], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.8], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.8], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0,0.8], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.8], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.8], mode="lines", name="STANDARD DEVIATION 3 END"))

#adding mean of sample data to the graph
fig.add_trace(go.Scatter(x=[sample_mean, sample_mean], y=[0, 0.8], mode="lines", name="SAMPLE MEAN"))
fig.show()

zscore = (sample_mean - mean)/std_deviation
print("Z score : " + str(zscore))

