import pandas as pd 
import numpy as np
import datetime
import time
import matplotlib.pyplot as plt
from functions import plot
from functions import custom
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
sleep['Hours of Sleep'] = sleep['Hours of Sleep'] + sleep['Naps']

############################### DATA CLEANING COMPLETE #########################################################

#Mean & Deviation of Mood and Sleep
avgmood = (round(sleep['Mood'].mean(), 2))
avgsleep = (round(sleep['Hours of Sleep'].mean(), 2))
devmood = (round(sleep['Mood'].std(), 2))
devsleep = (round(sleep['Hours of Sleep'].std(), 2))

#Making a new dataframe of only weekends
weekends = [sleep[sleep['Weekday'] == 'Saturday'], sleep[sleep['Weekday'] == 'Sunday']]
weekends = pd.concat(weekends)
weekends.sort_index(inplace = True)

#Making a new dataframe of only weekdays
wkdys = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekdays = sleep[sleep['Weekday'].isin(wkdys)]
weekdays.sort_index(inplace = True)

#Mean relations of weekends 
avgweekends = (round(weekends['Hours of Sleep'].mean(), 2))
moodweekends = (round(weekends['Hours of Sleep'].mean(), 2))

#Mean relations of weekdays
avgweekdays = (round(weekdays['Hours of Sleep'].mean(), 2))
moodweekdays = (round(weekdays['Hours of Sleep'].mean(), 2))

############################### DATA ANALYSING COMPLETE #########################################################

print('Project CIRCAN')
print('Analysis successful')
if devsleep > (1.5) or avgsleep < (7.50):
    print('You do not have a consistent number of hours of sleep.')
elif devsleep < (1.5) and avgsleep > (7.50):
    print('Congratulations! You have quite the healthy sleep routine!')

x = float(input("For an overall sleep analysis of all days, press 1. For a customized analysis of a chosen interval, press 2. To exit, press 3. "))

if x == 1:
    plot()

elif x == 2:
    custom()
else:
    print('Thank you. Hope you have a great day!')
