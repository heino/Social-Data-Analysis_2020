import os
__DIR__ = os.path.dirname(__file__)
ROOT = __DIR__ + '/../../..'
    

import numpy as np
import pandas as pd

indir = ROOT + '/data/raw/dolt'
outdir = ROOT + '/data/processed/dolt'

data_places = None
data_cases = None
data_details = None

def load():
    global data_places
    global data_cases
    global data_details

    data_places = pd.read_csv(
        indir + '/places.csv',
    #   names = ['place_id', 'country_region', 'province_state', 'latitude', 'longitude'],
        index_col='place_id',
        header=0,
        dtype = {
            'place_id': np.int64,
            'province_state': 'category',
            'country_region': 'category',
            'latitude': np.float64,
            'longitude': np.float64
        },
    )

    data_cases = pd.read_csv(
        indir + '/cases.csv',
    #   names = ['observation_time', 'place_id', 'confirmed_count', 'recovered_count', 'death_count'],
        index_col=['observation_time','place_id'],
        header=0,
        dtype = {
            'place_id': np.int64,
    #        'confirmed_count': np.int64, # Can't handle NaN
    #        'recovered_count': np.int64, # Can't handle NaN
    #        'death_count': np.int64      # Can't handle NaN
        },
        parse_dates = ['observation_time'],
    )

    data_datails = pd.read_csv(
        indir + '/case_details.csv',
    #   names = ['source', 'case_id', 'case_name', 'age', 'sex', 'nationality', 'current_status', 'symptomatic_date', 'confirmed_date', 'recovered_date', 'place_id'],
        index_col=['case_id'],
        header=0,
        dtype = {
            'source': 'category',
            'case_id': np.int64,
    #       'case_name': '',
    #       'age': np.int64,
    #       'sex': '',
            'nationality': 'category',
            'current_status': 'category',
    #       'symptomatic_date': 'datetime',
    #       'confirmed_date': 'datetime',
    #       'recovered_date': 'datetime',
            'place_id': np.int64,
        },
        parse_dates = {
            'symptomatic': ['symptomatic_date'],
            'confirmed': ['confirmed_date'],
            'recovered': ['recovered_date']
        },
    )

load()



if False:
    
    data_places.to_csv(
        outdir + '/places.csv',
        sep='|'
    )
    
    data_cases.to_csv(
        outdir + '/cases.csv',
        sep='|'
    )
    
    data_datails.to_csv(
        outdir + '/case_details.csv',
        sep='|'
    )
