import os
__DIR__ = os.path.dirname(__file__)
ROOT = __DIR__ + '/../../..'
    

import pandas as pd
import glob

indir = ROOT + '/data/raw/flights'
outdir = ROOT + '/data/processed/flights'

total = None
commercial = None

original_data= {}



def load():
    global total
    global commercial

    li = []

    for file in glob.glob(indir + "/number-of-commercial-fli*.csv"):
        li.append(
            pd.read_csv(
                file,
                names = [ 'date', '7day_average', 'count' ],
                header=0,
                sep = ';',
                parse_dates = [
                    'date',
                ], keep_date_col=False
            )
        )
        original_data[os.path.basename(file)] = pd.read_csv(file, sep=';')
    commercial = pd.concat(li, axis=0, ignore_index=True).drop_duplicates()
    commercial.set_index('date', inplace=True)


    li = []

    for file in glob.glob(indir + "/total-number-of-flights*.csv"):
        li.append(
            pd.read_csv(
                file,
                names = [ 'date', '7day_average', 'count' ],
                header=0,
                sep = ';',
                parse_dates = [
                    'date',
                ], keep_date_col=False
            )
        )
        original_data[os.path.basename(file)] = pd.read_csv(file, sep=';')

    total = pd.concat(li, axis=0, ignore_index=True).drop_duplicates()
    total.set_index('date', inplace=True)


def commercial():
    return commercial

def total():
    return total

def combined():
    combined = pd.merge(
        commercial,
        total,
        left_index=True, right_index=True,
        how='outer',
    )
    combined.columns=['commercial_7day_average', 'commercial', 'total_7day_average', 'total']
    return combined

load()
