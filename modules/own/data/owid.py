import os
__DIR__ = os.path.dirname(__file__)
ROOT = __DIR__ + '/../../..'
    

import pandas as pd
    


indir = ROOT + '/data/raw/testing'
outdir = ROOT + '/data/processed/testing'

data = None
data_raw = None

def load():
    global data
    global data_raw
    data_raw = data = pd.read_csv(indir + '/owid-covid-data.csv')
    data = pd.read_csv(
        indir + '/owid-covid-data.csv',
        usecols=["iso_code", "location", "date", "total_tests", "new_tests", "tests_units"],
        dtype = {
            'location': 'category',
            'iso_code': 'category'
        },
        parse_dates = ['date']
    )[["location", "iso_code", "date", "total_tests", "new_tests", "tests_units"]]
    data.columns = ['name','country', "date", "total_tests", "new_tests", "tests_units"]

    data.set_index(['date', 'country'], inplace=True)

def x():
    return data.drop(['name'], axis=1).set_index(['date', 'code']).unstack()

def countries():
    return data[['code', 'name']].set_index('code').drop_duplicates()


load()









# Make sure output dir exists
#if not os.path.exists(outdir):
#    os.mkdir(outdir)

if False:
    
    data.to_csv(
        outdir + '/cleaned.csv',
        sep='|'
    )

    owid_x['total'].to_csv(
        outdir + '/total_count.csv',
        sep='|'
    )

    owid_x['new'].to_csv(
        outdir + '/new_count.csv',
        sep='|'
    )

    owid_x['units'].to_csv(
        outdir + '/test_units.csv',
        sep='|'
    )

    owid_countries.to_csv(
        outdir + '/countries.csv',
        sep='|'
    )
