import os
__DIR__ = os.path.dirname(__file__)
ROOT = __DIR__ + '/../../..'

import pandas as pd
import glob
import own.data.ShouldItBePolish as ShouldItBePolish
import own.data.countries as Con

indir = ROOT + '/data/raw/hdi'

data = None
data_raw = None

def load():
    global data
    global data_raw
    data = pd.read_csv(indir + '/human-development-index.csv', header=0)
    data.columns = ['Country_name','Country_code', 'Year', 'HDI_value']
    data = data.drop_duplicates(subset = 'Country_code', keep = 'last')
    data = data.set_index('Country_code')
    data_raw = pd.read_csv(indir + '/human-development-index.csv', header=0)
#     data = pd.read_csv(indir + '/Human development index (HDI).csv')[['Country','2018']]
#     data = data[pd.to_numeric(data['2018'], errors='coerce').notnull()]
#     data['2018'] = pd.to_numeric(data['2018'])
#     data.rename(columns={'2018': 'HDI'}, inplace=True)

#     data.set_index('Country', inplace = True)

    
def ecdcWithHDI():
    dropped = ['cases', 'deaths', 'tests_new', 'region_code', 'subregion_code', 'offical_name', 'least_developed']
    sibp = ShouldItBePolish.with_per_capita().reset_index().dropna(subset=['tests_total'])
#     sibp = ShouldItBePolish.with_per_capita().reset_index().dropna(subset=['cases_total'])
    sibp = sibp.drop_duplicates(subset = 'country', keep = 'last').drop(dropped, axis = 1)
    sibp.set_index('country', inplace = True)
    merged = pd.merge(data,
            sibp,
            left_index=True, right_index=True,
            suffixes=('_HDI', '_sibp'),
            how='outer'
        )
    
    
    con = Con.geometries_110m().reset_index().set_index('iso3166_a3').drop(['geometry'], axis=1)
    merged = merged.merge(con,
            left_index=True, right_index=True,
            suffixes=('_HDI', '_sibp'),
            how='right'
        )
    dropped = ['id', 'iso3166_n3', 'name_en', 'name_long_en',
       'name_formal_en', 'label_rank', 'tiny', 'mapcolor_7', 'mapcolor_8', 'mapcolor_9', 'mapcolor_13']
    merged = merged.dropna(subset=['tests_total'])
#     merged = merged.dropna(subset=['cases_total'])

    merged = merged.drop(dropped, axis = 1).reset_index()
    merged = merged.dropna(subset = ['Country_name'])
    return merged
#     return merged

load()