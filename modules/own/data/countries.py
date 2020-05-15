import os
__DIR__ = os.path.dirname(__file__)
ROOT = __DIR__ + '/../../..'
    

import pandas as pd
import numpy as np
import geopandas as gpd
import json

    
indir = ROOT + '/data/raw/countries/'
outdir = ROOT + '/data/processed/countries/'

data = 'x'

def load():
    global data
    data = pd.read_csv(
        indir + 'country-codes_csv.csv',
        #    names = [ 'dateX', 'day', 'month', 'year', 'cases', 'deaths', 'name', 'code2', 'code3', 'population2018' ],
        #    header=0,
        na_values = '-99',
        usecols = [
            'ISO3166-1-Alpha-3',
            'ISO3166-1-Alpha-2',
            'ISO3166-1-numeric',
            'ITU',
            'official_name_en',

            'Continent',
            'Region Code',
            'Region Name',
            'Sub-region Code',
            'Sub-region Name',

            'ISO4217-currency_alphabetic_code',
            'ISO4217-currency_name',
            'ISO4217-currency_numeric_code',

            'CLDR display name',
            'Capital',

            'is_independent',
            'Developed / Developing Countries',
            'Least Developed Countries (LDC)',
        ],
        #    index_col = 'ISO3166-1-Alpha-3',
        dtype = {
            'Continent': 'category',

            'Region Code': 'category',
            'Region Name': 'category',
            'Sub-region Code': 'category',
            'Sub-region Name': 'category',
            'is_independent': 'category'
        },
    )
    data = data.replace({'Least Developed Countries (LDC)': {'x': True, np.NaN: False}})

    #countries_data#.describe


def regions():
    regions = data[['Region Code', 'Region Name']]
    regions.columns = ['code', 'name']

    regions = regions.drop_duplicates()
    regions.set_index('code', inplace=True)

    regions.dropna(inplace=True)

    return regions

def subregions():
    subregions = data[['Sub-region Code', 'Sub-region Name']]
    subregions.columns = ['code', 'name']

    subregions = subregions.drop_duplicates()
    subregions.set_index('code', inplace=True)

    subregions.dropna(inplace=True)

    return subregions

def continents():
    continent = data[['Continent']]
    continent.columns = ['name']

    continent = continent.drop_duplicates()
    continent.dropna(inplace=True)

    continent.reset_index(drop=True, inplace=True)

    return continent

def country_geography():
    x = data[['ISO3166-1-Alpha-3', 'Continent', 'Region Name', 'Sub-region Name', 'Region Code', 'Sub-region Code']]
    x.columns = ['country', 'continent', 'region_name', 'subregion_name', 'region_code', 'subregion_code']
    x.set_index('country', inplace=True)
    return x

def country_names():
    x = data[['ISO3166-1-Alpha-3', 'official_name_en', 'CLDR display name']]
    x.columns = ['country', 'offical_name', 'common_name']
    x.set_index('country', inplace=True)
    return x

def country_development():
    x = data[['ISO3166-1-Alpha-3', 'Developed / Developing Countries', 'Least Developed Countries (LDC)']]
    x.columns = ['country', 'development_type', 'least_developed']
    x.set_index('country', inplace=True)
    return x









def geometries_10m():
    return __geometries('10m')
def geometries_50m():
    return __geometries('50m')
def geometries_110m():
    return __geometries('110m')

def geometries_10m_json():
    return json.loads( __geometries('10m').to_json() )
def geometries_50m_json():
    return json.loads( __geometries('50m').to_json() )
def geometries_110m_json():
    return json.loads( __geometries('110m').to_json() )

''' https://geojson-maps.ash.ms '''
def __geometries(variant):

    # Load the maps geojson file
    df = gpd.read_file(indir + '../maps/geojson-maps.ash.ms/countries-'+variant+'.geojson')

    # Clean NaN's
    df.replace(['-99', -99], np.nan, inplace=True)


    # Transform columns into ordered categories
    from pandas.api.types import CategoricalDtype
    df['economy'] = df['economy'].astype(
        CategoricalDtype(categories=[
            '1. Developed region: G7',
            '2. Developed region: nonG7',
            '3. Emerging region: BRIC',
            '4. Emerging region: MIKT',
            '5. Emerging region: G20',
            '6. Developing region',
            '7. Least developed region',
        ], ordered=True)
    )
    df['income_grp'] = df['income_grp'].astype(
        CategoricalDtype(categories=[
            '5. Low income',
            '4. Lower middle income',
            '3. Upper middle income',
            '2. High income: nonOECD',
            '1. High income: OECD',
        ], ordered=True)
    )

    # Rename columns
    df.rename(columns = {
        'iso_a3': 'iso3166_a3',
        'iso_a2': 'iso3166_a2',
        'iso_n3': 'iso3166_n3',
        'name': 'name_en',
        'name_long': 'name_long_en',
        'formal_en': 'name_formal_en',
        'labelrank': 'label_rank',
        'mapcolor7': 'mapcolor_7',
        'mapcolor8': 'mapcolor_8',
        'mapcolor9': 'mapcolor_9',
        'mapcolor13': 'mapcolor_13',
        'income_grp': 'income_group'
    }, inplace=True)


    # Generate an index column (used for feature.id)
    df['id'] = df['adm0_a3']
    df.set_index('id', inplace=True)

    # Return
    return df[[
        'iso3166_a3', 'iso3166_a2', 'iso3166_n3',
        'name_en', 'name_long_en', 'name_formal_en',
        'label_rank', 'tiny',
        'mapcolor_7', 'mapcolor_8', 'mapcolor_9', 'mapcolor_13',
        'economy', 'income_group',
        'geometry'
    ]]


''' https://geojson-maps.ash.ms '''
def __geometries_OLD(variant):
    # Load the maps geojson file
    with open(indir + '../../maps/geojson-maps.ash.ms/countries-'+variant+'.geojson', 'r') as f:
        geojson = json.load(f)
    for feature in df['features']:

        for property in feature['properties']:
            if property == '-99':
                property = np.NaN

    return geojson


''' https://datahub.io/core/geo-countries '''
def __geometries_B():
    # Load the maps geojson file
    with open(indir + '/../maps/geojson', 'r') as f:
        geojson = json.load(f)

    # Add the missing 'id' feature. Copy the country code from inside properties
    for feature in geojson['features']:
        feature['id'] = feature['properties']['ISO_A3']

    return geojson
    
    


load()





# Make sure output dir exists
#if not os.path.exists(outdir):
#    os.mkdir(outdir)



