import os
__DIR__ = os.path.dirname(__file__)
ROOT = __DIR__ + '/../../..'

import pandas as pd

import own.data.ecdc as ECDC
import own.data.countries as Countries
import own.data.owid as OWID

def ecdc_totals():
    return ECDC.totals()

def ecdc_with_totals():
    return pd.concat((
        ECDC.data.drop(['continent', 'name', 'reported'], axis=1),
        ecdc_totals()
    ), axis=1)

def ecdc_with_totals_and_population():
    return pd.merge(
        ecdc_with_totals().reset_index().set_index('country'),
        ECDC.population(),
        left_index=True, right_index=True,
        how='left'
    ).reset_index().set_index(['date','country'])

def eced_with_total_and_tests():
    owid = OWID.data.drop('name', axis=1)
    owid.columns = ['tests_total', 'tests_new', 'tests_units']

    return pd.merge(
        ecdc_with_totals_and_population(),
        owid,
        left_index=True, right_index=True,
        suffixes=('_ecdc', '_owid'),
        how='outer'
    )

def with_countries():
    return pd.merge(
        eced_with_total_and_tests(),
        Countries.country_geography(),
        left_index=True, right_index=True,
        suffixes=('_ecdc', '_countries'),
        how='outer'
    )

def with_countries_names():
    return pd.merge(
        with_countries(),
        Countries.country_names(),
        left_index=True, right_index=True,
        suffixes=('_ecdc', '_countries'),
        how='outer'
    )

def with_development():
    return pd.merge(
        with_countries_names(),
        Countries.country_development(),
        left_index=True, right_index=True,
        suffixes=('_ecdc', '_countries'),
        how='outer'
    )

def with_per_capita():
    tests = with_development()
    tests['tests_per_capita'] = tests['tests_total'] / tests['population']
    return pd.merge(tests,
                    ECDC.per_capita(),
                    left_index=True, right_index=True,
                    suffixes=('_test', '_ecdc'),
                    how='outer')

