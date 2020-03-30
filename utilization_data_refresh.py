# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:22:27 2020

@author: DavidYoung
"""

import pandas as pd
from datetime import date

data_staging = r"C:\Users\DavidYoung\.spyder-py3\DataProject\staging"
archive = r"C:\Users\DavidYoung\.spyder-py3\DataProject\staging\archive"

def process_to_csv (df,file_name,file_dir):
    df.to_csv(file_dir + '\\' + file_name, index=False)

def process_date (cdc):
    col_sub = [df.columns[0]]
    df.dropna(axis=0, how='all', subset=col_sub, inplace=True)
    length = (len(df.columns))
    df.insert(length, 'ProcessDate', date)
    return df

date = date.today()

links={'CDC':'https://covid.ourworldindata.org/data/full_data.csv'}
data = links["CDC"]
df = pd.read_csv(data)

process_date(df)

df.head()
#process to archive file(s)
process_to_csv(df, "cdc_covid_data"+ str(date)+ ".csv",archive )
#process to staging file(s)
process_to_csv(df, "cdc_covid_data.csv",data_staging )