import os
__DIR__ = os.path.dirname(__file__)
ROOT = __DIR__ + '/../../..'
    

import pandas as pd


indir = ROOT + '/data/raw/gas'
outdir = ROOT + '/data/processed/gas'

data = None

def load():
    global data
    data = pd.read_csv(
        indir + '/daily_csv.csv',
        index_col = 'Date',
        parse_dates = ['Date'], keep_date_col=True
    )


load()
