import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime

def graph_test(dictionary=test):
    for i in range(len(dictionary)):
        data = dictionary[i]
        if data == 'user input':
            time= np.array([dictionary[i][df][6] for df in range(len(dictionary[i]))])#the 3rd index [6] is the current index for time
            parameter= np.array([dictionary[i][df][4] for df in range(len(dictionary[i]))])#[4] the data to measure parameter 
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


