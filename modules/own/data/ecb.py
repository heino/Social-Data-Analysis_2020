import os
__DIR__ = os.path.dirname(__file__)
ROOT = __DIR__ + '/../../..'
    

import pandas as pd
    

indir = ROOT + '/data/raw/ecb'
outdir = ROOT + '/data/processed/ecb'

data = None

def load():
    global data
    data = pd.read_csv(
        indir + '/eurofxref-hist.csv',
        index_col = 'Date',
        parse_dates = ['Date'], keep_date_col=True
    )
    data.drop(['Unnamed: 42'], axis=1, inplace=True)
        
        
load()
