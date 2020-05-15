import os
__DIR__ = os.path.dirname(__file__)
ROOT = __DIR__ + '/../../..'
    
import pandas as pd
    
indir = ROOT + '/data/raw/nasdaq'



def load():

    data = pd.read_csv(
        indir + '/nasdaq.csv'
    )[['Date', 'Close']]
    
    data.Date = pd.to_datetime(data.Date, format='%d/%m/%Y')
    return data
#     data_merged = pd.merge(
#         data_brent, data_twi,
#         left_index=True, right_index=True,
#         suffixes=('_Brent', '_Twi'),
#         how='outer'
#     )
#     data_merged.columns = ['Breant', 'Twi']
#     data_merged['Average'] = data_merged.mean(numeric_only=True, axis=1)

load()

