import os
__DIR__ = os.path.dirname(__file__)
ROOT = __DIR__ + '/../../..'
    

import pandas as pd
import numpy as np
    
indir = ROOT + '/data/raw/ecdc/'
outdir = ROOT + '/data/processed/ecdc/'

data = None;
population2018 = None

def load():
    global data
    data = pd.read_csv(
        indir + 'ecdc.csv',
        names = [ 'dateRep', 'day', 'month', 'year', 'cases', 'deaths', 'name', 'code2', 'code3', 'population2018', 'continent' ],
        header=0,
        #index_col=['date', 'code3'],
        dtype = {
            'name': 'category',
            'code2': 'category',
            'code3': 'category',
            'continent': 'category'
        },
        parse_dates = {
            'date': ['year', 'month', 'day'],
            'reported': ['dateRep']
        }, keep_date_col=False
    )

    # Following countries are missing 2 char country codes (= lost when dropping NaN):
    # - Namibia

    data = data[ data['code2'].notnull()]

    # Following countries are missing 3 char country codes (= lost when dropping NaN):
    # - Anguilla
    # - Bonaire, Saint Eustatius and Saba
    # - Cases_on_an_international_conveyance_Japan
    # - Czechia
    # - Falkland_Islands_(Malvinas)

    data = data[ data['code3'].notnull()]


    data.drop(['code2'], axis=1, inplace=True)
    data.rename(columns={'code3': 'country'}, inplace=True)
    

    global population2018

    population2018 = data[['country', 'population2018']].drop_duplicates()
    population2018.rename({'population2018': 'population'}, axis=1, inplace=True)
    population2018.set_index('country', inplace=True)

    data.drop(['population2018'], axis=1, inplace=True)
    

    data.set_index(['date', 'country'], inplace=True)


def count():
    return data[['cases', 'deaths']]

def totals():
    df = data[['cases', 'deaths']].unstack().cumsum().stack()
    df.columns = ['cases_total', 'deaths_total']
    return df

def totals_with_per_capita():
    df = pd.merge(
        totals(),
        population(),
        left_index=True, right_index=True,
        how='left'
    )#.reset_index().set_index(['date','country'])

    df['cases_total_per_capita'] = df['cases_total'] / df['population']
    df['deaths_total_per_capita'] = df['deaths_total'] / df['population']

    df.drop(['population'], axis=1, inplace=True)

    return df

def per_capita():
    df = totals_with_per_capita()
    df.drop(['cases_total', 'deaths_total'], axis=1, inplace=True)
    return df

def count_with_totals_and_per_capita():
    return pd.merge(
        count(),
        totals_with_per_capita(),
        left_index=True, right_index=True,
        how='left'
    )#.reset_index().set_index(['date','country'])


def first_death_date_per_country():
    first_death = pd.DataFrame(columns={'country', 'date'})
    first_death['date'] = pd.to_datetime(first_death['date'])
    first_death.set_index('country', inplace=True)

    deathsX = deaths().unstack();
    
    for country in deathsX.keys():
        series = deathsX[country]
        x = series[series.ge(1)]
        if len(x) > 0:
            date = x.idxmin()
        else:
            date = np.NaN
        first_death.loc[country] = date

    return first_death



def cases_and_deaths():
    return data.drop(['name', 'reported', 'continent' ], axis=1)

def cases():
    return cases_and_deaths()['cases']

def deaths():
    return cases_and_deaths()['deaths']

def countries():
    return data.reset_index()[['country', 'name']].set_index('country').drop_duplicates()

def population():
    return population2018




load()








if False:
    
    OWID.data.to_csv(
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

    
    
    
    
    
    
    
    
    
# Make sure output dir exists
#if not os.path.exists(outdir):
#    os.mkdir(outdir)
    
if False:
    cases_and_deaths()['cases'].unstack().to_csv(
        outdir + 'cases.csv',
        sep='|'
    )

    cases_and_deaths()['deaths'].unstack().to_csv(
        outdir + 'deaths.csv',
        sep='|'
    )

    #cases_and_deaths()['cases'].unstack()['DNK'].to_csv(
    #    'python/cases-DNK.csv',
    #    sep='|'
    #)
    
    
if False:
    countries().to_csv(
        outdir + 'countries.csv',
        sep='|'
    )
