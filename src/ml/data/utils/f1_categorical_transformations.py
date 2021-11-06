import pandas as pd
import numpy as np

# Must discuss with Clark to decide on a per feature basis.
def insert_zeroes(df):
    return df.replace('Unknown', 0)

'''
def insert_zeroes(df, col, encoding):
    return df[col].replace('Unknown', encoding)
'''

def get_one_hot_features():
    return [
        'Race',
        'Marital Status - Injury',
        'Education - Injury',   # ordinal
        'Occupation Status - Injury',
        'Occupation Code - Injury',
        'Primary Insurance',
        'Anxiety - History',
        'Neurologic Category - Admission',
        'Level of Injury - Admission' # ordinal
    ]

def get_ordinal_features():
    return {
        'Injury Date' : None, # no unknowns
        'Height - Admission' : None, # unknown = median
        'Weight - Admission' : None, # unknown = median
        'Age - Injury' : { # unknown = mode
            '0-14y' : 1,
            '15-29y' : 2,
            '30-44y' : 3,
            '45-59y' : 4,
            '60-74y' : 5,
            '75+y' : 6
        },
        'Daily Alcohol - History' : { # unknown = 0
            '0' : 1,
            '1-2' : 2,
            '3-4' : 3,
            '5-6' : 4,
            '7-9' : 5,
            '10+' : 6
        },
        'ASIA - Admission' : { # one hot
            'A' : 1,
            'B' : 2,
            'C' : 3,
            'D' : 4,
            'E' : 5
        },
        'ASIA - Discharge' : { # # unknown = DROP ROWS
            'A' : 1,
            'B' : 2,
            'C' : 3,
            'D' : 4,
            'E' : 5
        },
        'Loss of Consciousness - Injury' : { # unknown = 1
            'False' : 1,
            '<=30min' : 2,
            '31min-24hrs' : 3,
            '24hrs+' : 4
        },
        'TBI Likelihood - Injury' : { # unknown = 1
            'Improbable' : 1,
            'Possible' : 2,
            'Mild' : 3,
            'Moderate' : 4,
            'Severe' : 5
        },
        # The ones below could be booleans but the NaNs really hurt us.
        'Sex' : { # one hot if lots of unknowns (make "other" unknown), drop "other" if no unknowns and make this bool
            'Male' : 1, 
            'Female' : 2,
            'Other' : 3
        },
        'Veteran' : { # unknown = false
            'False' : 1,
            'True' : 2
        },
        'Depression - History' : { # unknown = false
            'False' : 1,
            'True' : 2
        },
        'Diabetes - History' : { # unknown = false
            'False' : 1,
            'Medication Controlled' : 2,
            'Lifestyle Controlled' : 2,
            'Not Controlled' : 2,
            'Unknown If Controlled' : 2
        },
        'Loss of Memory - Injury' : { # unknown = false
            'False' : 1,
            'True' : 2
        }
    }

def transform_one_hot(df):
    for feature in get_one_hot_features():
        df = pd.get_dummies(df, columns = [feature])
    return df

def transform_ordinal(df):
    for feature, mapping in get_ordinal_features().items():
        if mapping is not None:
            df.replace({feature : mapping}, inplace=True)
        # Need the double cast to workaround library bug.
        # See here: https://stackoverflow.com/questions/60024262/error-converting-object-string-to-int32-typeerror-object-cannot-be-converted
        df[feature] = df[feature].astype('float').astype('int64')
        
# I didn't bother transforming default ignored columns in dataset_loader.get_dataset_df_x_y().
def transform_all(df):
    df = insert_zeroes(df)
    transform_ordinal(df)
    return transform_one_hot(df)
