#import dataset and required packages for data analysis
import pandas as pd
import csv
import numpy as np


def read_data():

    path ='ChicagoWeatherChristmas.csv'
    df = pd.read_csv(path)

    df.replace("Not Defined", np.NaN)
    df.dropna(inplace=True)

    # rename
    df.columns = ['Jahr', 'Fahrenheit High Temp', 'Fahrenheit Min Temp', 'Niederschlag',
           'Snow', 'Weiße Weihnachten', 'T min', 'T max']

    # select
    feature_names = ['Jahr', 'Niederschlag', 'T min', 'T max']
    target_name = 'Weiße Weihnachten'
    columns_subset = [target_name] + feature_names
    df = df[columns_subset]
    
    # string to bool
    df['Weiße Weihnachten'] = df['Weiße Weihnachten'] == "TRUE"
    
    
    return df, target_name, feature_names