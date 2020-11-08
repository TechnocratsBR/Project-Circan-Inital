import pandas as pd
from openpyxl import load_workbook
from logfunctions import openxlsx
import sys
from gui import *

openxlsx()


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
    
