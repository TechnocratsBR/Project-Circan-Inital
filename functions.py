import pandas as pd 
import numpy as np
import datetime
import time
import matplotlib.pyplot as plt
import seaborn

# Reading and cleaning the data
sleep = pd.read_excel('circanlog.xlsx')
#New column which shows name of day
sleep['Weekday'] = sleep['Days'].dt.day_name()
#Converting format of columns to [datetime64]
sleep['Days']= pd.to_datetime(sleep['Days'])
sleep['Wake'] = pd.to_datetime(sleep['Wake'])
sleep['Sleep'] = pd.to_datetime(sleep['Sleep'])
sleep.dropna(inplace = True)

#New column which states the number of hours slept
sleep['Hours of Sleep'] = (abs(sleep['Sleep'] -sleep['Wake']))
#Converting it to hours and rounding it to 2 decimals
sleep['Hours of Sleep'] = sleep['Hours of Sleep']/np.timedelta64(1,'h')
sleep['Hours of Sleep'] = round(sleep['Hours of Sleep'], 2)
sleep['Hours of Sleep'] = sleep['Hours of Sleep'] - sleep['Naps']

############################### DATA CLEANING COMPLETE #########################################################

#Plotting the relations
def plot():
    seaborn.set()
    plt.figure()
    plt.subplot(211)
    plt.axhline(y=15000, color='g', linestyle=':')
    plt.plot(sleep.index, sleep['Steps'], 'g', label = 'Steps')
    ax = plt.gca()
    ax.legend(loc = 'upper left')

    plt.subplot(212)
    plt.axhline(y=8.0, color='b', linestyle=':')
    plt.axhline(y=2.0, color='r', linestyle=':')
    plt.plot(sleep.index, sleep['Mood'], 'r', label = 'Mood')
    plt.plot(sleep.index, sleep['Hours of Sleep'], 'b', label = 'Hours of Sleep')
    ax = plt.gca()
    ax.legend(loc = 'upper left')
    
    return plt.show()

#Defining and plotting custom dates
def custom():
    seaborn.set()
    num_1 = int(input('Please input the index of the date you would like to start from: '))
    num_2 = int(input('Till: '))
    diff = abs(num_2 - num_1) + 1
    cust = np.linspace(num_1, num_2, num = diff).tolist()
    customdays = sleep[sleep.index.isin(cust)]
    plt.figure()
    plt.subplot(211)
    plt.axhline(y=15000, color='g', linestyle=':')
    plt.plot(customdays.index, customdays['Steps'], 'g', label = 'Steps')
    ax = plt.gca()
    ax.legend(loc = 'upper left')

    plt.subplot(212)
    plt.axhline(y=8.0, color='b', linestyle=':')
    plt.axhline(y=2.0, color='r', linestyle=':')
    plt.plot(customdays.index, customdays['Mood'], 'r', label = 'Mood')
    plt.plot(customdays.index, customdays['Hours of Sleep'], 'b', label = 'Hours of Sleep')
    ax = plt.gca()
    ax.legend(loc = 'upper left')

    return plt.show()
    


