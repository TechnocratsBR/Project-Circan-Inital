import pandas as pd
from openpyxl import load_workbook
from logfunctions import openxlsx
import sys
from gui import *
import os.path

if os.path.isfile('circanlog.xlsx') is False:
    openxlsx()

while True:
<<<<<<< HEAD
    day = input("Please input today's date (eg. 1-Aug-20): ")
    sleep = input("At what time did you exactly sleep? ")
    wake = input("What time did you wake up? ")
    naps = input('Did you take a nap? If so, how long? ')
    steps = input("How many steps did you take today? ")
    mood = input("How was your mood? ")
    cont = input("Would you like to add more data? ")

=======
>>>>>>> a517107407832b56310ad8332fecd542f5909e22
    # new dataframe with same columns
    df = pd.DataFrame({'Days': [day],
                    'Sleep': [sleep],
                    'Wake': [wake],
                    'Naps': [naps],
                    'Steps': [steps],
                    'Mood': [mood],                  
                    })
    writer = pd.ExcelWriter('circanlog.xlsx', engine='openpyxl')
    # try to open an existing workbook
    writer.book = load_workbook('circanlog.xlsx')
    # copy existing sheets
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    # read existing file
    reader = pd.read_excel(r'circanlog.xlsx')
    # write out the new sheet
    df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)

    writer.close()
    
    if cont == 'No':
        break
        sys.exit()
