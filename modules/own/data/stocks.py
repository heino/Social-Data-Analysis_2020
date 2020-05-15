import os
__DIR__ = os.path.dirname(__file__)
ROOT = __DIR__ + '/../../..'
    

import pandas as pd
    
indir = ROOT + '/data/raw/stocks/'
outdir = ROOT + '/data/processed/stocks/'

data = None;

def load():
    global data

    df = pd.read_excel(
        indir + 'Markets.xlsx',
        header=0,
    )

    df.rename(columns={
        'Index ': 'index',
        'ISO3166-1-Alpha-3': 'country',
    }, inplace=True)

    df['index'] = df['index'].str.rstrip(' Index')

    data = df


def valuesByCountry():
    df = data.drop(columns={'index', 'Country/Region'}).set_index(['country']).transpose()
    df.index.name = 'date'
    df.index = pd.to_datetime(df.index)
    return df

def valuesByIndex():
    df = data.drop(columns={'country', 'Country/Region'}).set_index(['index']).transpose()
    df.index.name = 'date'
    df.index = pd.to_datetime(df.index)
    return df

def indexCountries():
    return data[['index', 'country']].drop_duplicates().reset_index(drop=True)

load()
