import os
__DIR__ = os.path.dirname(__file__)
ROOT = __DIR__ + '/../../..'
    

import pandas as pd
import json

indir = ROOT + '/data/raw/stocks'
outdir = ROOT + '/data/processed/stocks'

countries = [
#    'AUS',
#    'AUT',
   'BEL',
#    'BRA',
#    'CAN',
#    'CHE',
    'CHN',
    'DEU',
    'DNK',
    'ESP',
#    'FIN',
    'FRA',
    'GBR',
#    'GRC',
#    'IND',
#    'IRL',
#    'ISL',
#    'ISR',
    'ITA',
#    'JPN',
#    'KOR',
#    'MEX',
#    'NLD',
#    'NZL',
#    'POL',
#    'PRT',
#    'RUS',
#    'SGP',
    'SWE',
#    'TWN',
    'USA',
#    'ZAF',

#    'HKG',

#    'NOR',
]



stocks_data = {}
index_names = {}

def load():
    global stocks_data
    global index_names
    for country in countries:
        with open(indir + '/' + country + '.json') as json_file:
            data = json.load(json_file)
        
            df = pd.DataFrame(data['series'][0]['data'])
            df['date'] = pd.to_datetime(df['date'])
            
            df.set_index('date', inplace=True)
        
            stocks_data[country] = df
            index_names[country] = data['series'][0]['full_name']
            


        
def close_values():
    df = pd.DataFrame(columns=['date'])
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    for country in countries:
        value = stocks_data[country]['close']
        value.name = country

        df = df.merge(
            value.to_frame(),
            left_index=True,
            right_index=True,
            how = 'right'
        )

    return df
        

    
    
    
load()
