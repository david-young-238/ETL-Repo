'''
Author: David Young
Date:2.18.2020

WM dataset processing date and file hydration
'''

import pandas as pd
from datetime import date

'''
Write to csv
'''

def process_to_csv (df,file_name,file_dir):
    df.to_csv(file_dir + '\\' + file_name, index=False)


"""
Process Date
"""

def process_date (df):
    col_sub = [df.columns[0]]
    df.dropna(axis=0, how='all', subset=col_sub, inplace=True)
    length = (len(df.columns))
    df.insert(length, 'ProcessDate', date)
    return df.copy()
    #  for i in df.index:
    #    val = df.iat(i, length)
    #    if math.isnan(val):
    #        df.set_value( i,'ProcessDate', date, -1)
   
'''
Config
'''

date = date.today()

dir_loc = ( r"C:\Users\DavidYoung\Box\My Documents\Local Reporting Files\Engagements\Walmart\WM Production File\SourceData")
file_name = "Weekly Production Report 01.24.20 FINAL - DO NOT EDIT.xlsm"
data_staging = r"C:\Users\DavidYoung\Box\My Documents\Local Reporting Files\Engagements\Walmart\WM Production File\DatabaseStagingFiles"
archive = r"C:\Users\DavidYoung\Box\My Documents\Local Reporting Files\Engagements\Walmart\WM Production File\Archive"

with pd.ExcelFile(dir_loc + '\\' + file_name) as xlms:
    alert_raw = pd.read_excel(xlms, 'Alert Prod')
    df1 = alert_raw[["Alert ID","Party Number","Alert Create Date","Alert Status","Scenario Category","Alert Subcategory","Alert Run Date","Alert Close Date","Scenario Name","Alert Investigator","Alert Investigator User Name","Alert Due Date","Case Investigator"]].copy() #Create copy to reduce ambiguity between alert_raw and df1 dataframes
    case_raw = pd.read_excel(xlms, 'Case Prod')
    df2 = case_raw[["Case ID","Party Number","Case Status","Case Create DTTM (1)","Case Close DTTM (1)","Case Disposition","Case Investigator Name","Case Investigator","Case Creator"]].copy()
    sar_raw = pd.read_excel(xlms, 'SAR')
    df3 = sar_raw[["Case ID","Case Create DTTM","Case Status","Investigator Name","Investigator User Name","SAR Create Date"]].copy()

"""
Add Processing Date
"""

process_date(df1)
process_date(df2)
process_date(df3)

"""
Process To File for Database hydration
"""

#process to archive files
process_to_csv(df1, "alert_production_"+ str(date)+ ".csv",archive )
#process to staging files
process_to_csv(df1, "alert_production.csv",data_staging )
#process to archive files
process_to_csv(df2, "case_production_"+ str(date)+ ".csv",archive )
#process to staging files
process_to_csv(df2, "case_production.csv",data_staging )
#process to archive files
process_to_csv(df3, "sar_production_"+ str(date)+ ".csv",archive )
#process to staging files
process_to_csv(df3, "sar_production.csv",data_staging )