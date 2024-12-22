#!/opt/anaconda3/bin/python3.12

import pandas as pd
import sqlite3
import logging

logger= logging.getLogger()

logging.basicConfig(
    filename='log.log',
    format='[%(asctime)s][%(levelname)s]%(message)s',
    level=logging.INFO,
    datefmt='%y-%m-%d %H:%M')
logger.info('Running script...')

df = pd.read_csv('Automobile.csv')
con = sqlite3.connect('Automobile.db')
print(df.head())

filtered_df = df[df['horsepower'] > 190]
print(filtered_df)
filtered_df.to_sql('AutomobileHorseP', con, if_exists='append', index=False)

import os
print(os.getcwd())

def is_correlation_true(df: pd.DataFrame) -> bool :
    acceleration = df.acceleration
    horsepower = df.horsepower
    
    if 'horsepower' not in df.columns or 'acceleration' not in df.columns:
        raise ValueError("Dataframe does not contain 'horsepower' / 'acceleration'. ")
    correlation_value = df['horsepower'].corr(df['acceleration'])
    return correlation_value < 0 

is_correlation_true(filtered_df)

def compare_avg_hk_origin(df):
    horsepower = df.horsepower
    origin = df.origin
    acceleration = df.acceleration
    
    
    if 'horsepower' not in df.columns or 'origin' not in df.columns:
        raise ValueError("Dataframe does not contain 'horsepower' / 'origin'. ")
    
    if not horsepower.dtype == float:
        raise TypeError("must contain numeric data!")
    if not origin.dtype == object:
        raise TypeError("must contain string data!")
     
    usa_cars = df[df['origin'] == 'usa']
    european_cars = df[df['origin'] == 'european']
    avg_horsepower_usa = usa_cars['horsepower'].mean()
    avg_horsepower_european = european_cars['horsepower'].mean()
 
    if avg_horsepower_usa > avg_horsepower_european:
     print("American cars have a higher horsepower average compared to european cars.")
    else:
     print("European cars have a higher horsepower average comapared to the american cars.") 
     
     print(compare_avg_hk_origin(df))