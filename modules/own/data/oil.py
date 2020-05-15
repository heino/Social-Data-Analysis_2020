import os
__DIR__ = os.path.dirname(__file__)
ROOT = __DIR__ + '/../../..'
    

import pandas as pd
    

indir = ROOT + '/data/raw/oil'
outdir = ROOT + '/data/processed/oil'


data_brent = None
data_twi = None

data_merged = None

def load():
    global data_brent
    global data_twi
    global data_merged

    data_brent = pd.read_csv(
        indir + '/brent-daily_csv.csv',
        index_col = 'Date',
        parse_dates = ['Date'], keep_date_col=True
    )

    data_twi = pd.read_csv(
        indir + '/wti-daily_csv.csv',
        index_col = 'Date',
        parse_dates = ['Date'], keep_date_col=True
    )

    data_merged = pd.merge(
        data_brent, data_twi,
        left_index=True, right_index=True,
        suffixes=('_Brent', '_Twi'),
        how='outer'
    )
    data_merged.columns = ['Breant', 'Twi']
    data_merged['Average'] = data_merged.mean(numeric_only=True, axis=1)

load()

