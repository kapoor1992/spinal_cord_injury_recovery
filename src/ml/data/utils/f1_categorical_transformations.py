import pandas as pd
import numpy as np

def get_one_hot_features():
    return [
        'Race',
        'Marital Status - Injury',
        'Occupation Status - Injury',
        'Primary Insurance',
        'Anxiety - History',
        'Neurologic Category - Admission',
        'ASIA - Admission'
    ]

def get_bool_features():
    return {
        'Veteran' : {
            'False' : False,
            'True' : True,
            'Unknown' : False
        },
        'Depression - History' : {
            'False' : False,
            'True' : True,
            'Unknown' : False
        },
        'Diabetes - History' : {
            'False' : False,
            'Medication Controlled' : True,
            'Lifestyle Controlled' : True,
            'Not Controlled' : True,
            'Unknown If Controlled' : True,
            'Unknown' : False
        },
        'Loss of Memory - Injury' : {
            'False' : False,
            'True' : True,
            'Unknown' : False
        },
        'Sex' : {
            'Male' : False, 
            'Female' : True,
            'Other' : False # Only two in dataset, just map to male.
        }
    }

def get_ordinal_features_to_impute():
    return {
        'Education - Injury' : {
            'Less Than 9th Grade' : 1,
            '9th-11th Grade' : 2,
            'High School' : 3,
            'Associate Degree' : 4,
            'Bachelors Degree' : 5,
            'Masters Degree' : 6,
            'Doctorate' : 7,
            'Other' : 3, # This is the mode. Hardcoding value so we don't need to query old mode during inference time.
            'Unknown' : 3 # Same as above.
        }
    }

def get_ordinal_features():
    return {
        'Injury Date' : None,
        'Age - Injury' : {
            '0-14y' : 1,
            '15-29y' : 2,
            '30-44y' : 3,
            '45-59y' : 4,
            '60-74y' : 5,
            '75+y' : 6
        },
        'Daily Alcohol - History' : {
            '0' : 1,
            '1-2' : 2,
            '3-4' : 3,
            '5-6' : 4,
            '7-9' : 5,
            '10+' : 6,
            'Unknown' : 1
        },
        'ASIA - Discharge' : {
            'A' : 1,
            'B' : 2,
            'C' : 3,
            'D' : 4,
            'E' : 5
        },
        'Loss of Consciousness - Injury' : {
            'False' : 1,
            '<=30min' : 2,
            '31min-24hrs' : 3,
            '24hrs+' : 4,
            'Unknown' : 1
        },
        'TBI Likelihood - Injury' : {
            'Improbable' : 1,
            'Possible' : 2,
            'Mild' : 3,
            'Moderate' : 4,
            'Severe' : 5,
            'Unknown' : 1
        },
        'Level of Injury - Admission' : {
            'C01' : 1,
            'C02' : 2,
            'C03' : 3,
            'C04' : 4,
            'C05' : 5,
            'C06' : 6,
            'C07' : 7,
            'C08' : 8,
            'T01' : 9,
            'T02' : 10,
            'T03' : 11,
            'T04' : 12,
            'T05' : 13,
            'T06' : 14,
            'T07' : 15,
            'T08' : 16,
            'T09' : 17,
            'T10' : 18,
            'T11' : 19,
            'T12' : 20,
            'L01' : 21,
            'L02' : 22,
            'L03' : 23,
            'L04' : 24,
            'L05' : 25,
            'S01' : 26,
            'S02' : 27,
            'S03' : 28,
            'S04' : 29,
            'S05' : 30,
            'c01' : 1,
            'c02' : 2,
            'c03' : 3,
            'c04' : 4,
            'c05' : 5,
            'c06' : 6,
            'c07' : 7,
            'c08' : 8,
            't01' : 9,
            't02' : 10,
            't03' : 11,
            't04' : 12,
            't05' : 13,
            't06' : 14,
            't07' : 15,
            't08' : 16,
            't09' : 17,
            't10' : 18,
            't11' : 19,
            't12' : 20,
            'l01' : 21,
            'l02' : 22,
            'l03' : 23,
            'l04' : 24,
            'l05' : 25,
            's01' : 26,
            's02' : 27,
            's03' : 28,
            's04' : 29,
            's05' : 30
        }
    }

def transform_bool(df):
    for feature, mapping in get_bool_features().items():
        df.replace({feature : mapping}, inplace=True)
        df[feature] = df[feature].astype('boolean')


def transform_one_hot(df):
    for feature in get_one_hot_features():
        df = pd.get_dummies(df, columns = [feature])
    return df

def transform_imputed_ordinal(df):
    for feature, mapping in get_ordinal_features_to_impute().items():
        df.replace({feature : mapping}, inplace=True)

        # Dormant for now.
        df[feature].replace('mode', np.nan, inplace=True)
        df[feature].fillna(df[feature].mode().iloc[0], inplace=True)
        
        df[feature] = df[feature].astype('int64')

def transform_ordinal(df, inference_usage=False):
    for feature, mapping in get_ordinal_features().items():
        # We don't need these at inference time.
        if inference_usage and (feature == 'Injury Date' or feature == 'ASIA - Discharge'):
            continue

        if mapping is not None:
            df.replace({feature : mapping}, inplace=True)
        # Need the double cast to workaround library bug.
        # See here: https://stackoverflow.com/questions/60024262/error-converting-object-string-to-int32-typeerror-object-cannot-be-converted
        df[feature] = df[feature].astype('float').astype('int64')
        
# I didn't bother transforming default ignored columns in dataset_loader.get_dataset_df_x_y().
def transform_all(df):
    transform_bool(df)
    transform_ordinal(df)
    transform_imputed_ordinal(df)
    return transform_one_hot(df)
