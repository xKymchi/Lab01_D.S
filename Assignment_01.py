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
