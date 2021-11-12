import sys
sys.path.append('..')
import data.utils.f1_categorical_transformations as f1_categorical_transformations
import pandas as pd
import pickle

def json_to_df(json_model, expected_features):
    df = pd.DataFrame([json_model])

    f1_categorical_transformations.transform_bool(df)
    f1_categorical_transformations.transform_imputed_ordinal(df)
    f1_categorical_transformations.transform_ordinal(df, inference_usage=True)
    df = f1_categorical_transformations.transform_one_hot(df)

    zeroed_one_hot_features = list(set(expected_features) - set(list(df.columns.values)))
    
    for feature in zeroed_one_hot_features:
        df[feature] = 0

    return df

def infer(json_model, pickle_path):
    with open(pickle_path, 'rb') as f:
        clf = pickle.load(f)
    
    df = json_to_df(json_model, clf.inference_features)
    prediction = clf.predict(df)[0]

    asia_mapper = f1_categorical_transformations.get_ordinal_features()['ASIA - Discharge']
    reverse_asia_mapper = {v: k for k, v in asia_mapper.items()}
    
    return reverse_asia_mapper[prediction]

json_model = {
    "Age - Injury" : "15-29y",
    "Sex" : "Male",
    "Level of Injury - Admission" : "C05",
    "Education - Injury" : "High School",
    "Veteran" : "False",
    "Depression - History" : "False",
    "Diabetes - History" : "False",
    "Daily Alcohol - History" : "0",
    "Loss of Consciousness - Injury" : "<=30min",
    "Loss of Memory - Injury" : "False",
    "TBI Likelihood - Injury" : "Improbable",
    "Race" : "Asian",
    "Marital Status - Injury" : "Never Married",
    "Occupation Status - Injury" : "Working",
    "Occupation Code - Injury" : "Service",
    "Primary Insurance" : "Other Government",
    "Anxiety - History" : "False",
    "Neurologic Category - Admission" : "Incomplete Tetraplegic",
    "ASIA - Admission" : "B"
}

print(infer(json_model, 'pickles/random_forest.pkl'))