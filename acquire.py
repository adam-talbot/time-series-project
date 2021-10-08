import pandas as pd
import numpy as np
import os

def C_to_F(temp):
    '''
    Converts temp from C to F
    '''
    return (temp * (9/5) + 32)

def get_data():
    '''
    Gets data from csv, filters to Phoenix, sets datetime index, only pulls temperature column, converts from C to F
    '''
    df = pd.read_csv('GlobalLandTemperaturesByCity.csv')
    df = df[df.City == 'Phoenix']
    df = df.rename(columns={'AverageTemperature' : 'avg_temp', 'dt' : 'Date'})
    df.Date = pd.to_datetime(df.Date)
    df = df.set_index('Date')
    df = df.sort_index()
    df = df[['avg_temp']]    
    df = df.apply(C_to_F)
    df = df['2008': '2012']
    return df
    


