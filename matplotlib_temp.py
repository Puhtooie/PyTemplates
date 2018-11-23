import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime

def graph_test(dictionary=test):
    for pandas_df in range(len(dictionary)):
        data = dictionary[pandas_df]
        if data == 'user input':
            time= dictionary[pandas_df][0]#the 3rd index [6] is the current index for time
            parameter= dictionary[pandas_df][1]#[4] the data to measure parameter 
            for t in range(len(time)):
                time[t]= datetime.utcfromtimestamp(time[t] // 1000)
                # high, low query to compute profit/loss
                    #Make this take objects in a loop
            plt.plot(time,parameter)
                   #symbol must be str
            plt.title(data)
            plt.xlabel('time')
            plt.ylabel('paramter')
            plt.show()


