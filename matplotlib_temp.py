import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
from matplotlib import style

style.use('ggplot')

def graph_test(dictionary=test):
    for pandas_df in range(len(dictionary)):
        data = dictionary[pandas_df]
        
        if data == 'user input':
            time= dictionary[pandas_df][0]#the 3rd index [6] is the current index for time
            parameter= dictionary[pandas_df][1]#[4] the data to measure parameter 
            
            #comment out this section if you already have switched from milliseconds to Date-time
            for t in range(len(time)):
                time[t]= datetime.utcfromtimestamp(time[t] // 1000)

            plt.plot(time,parameter)
            plt.title(data)
            plt.xlabel('time')
            plt.ylabel('paramter')
            plt.show()


