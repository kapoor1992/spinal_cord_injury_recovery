import pandas as pd
import data.utils.f1_feature_translations as f1_feature_translations
import data.utils.f1_categorical_transformations as f1_categorical_transformations
import data.utils.f1_inclusion_cols as f1_inclusion_cols

def load_dataset(input_path, output_path):
    cols_to_use = f1_inclusion_cols.get_inclusion_x_cols() + f1_inclusion_cols.get_inclusion_y_cols()
    df = pd.read_csv(input_path, usecols=cols_to_use, dtype=str).fillna('Unknown')
    print(f'input dataset loaded from {input_path}')

    translations = f1_feature_translations.get_translations()

    for key, translation in translations.items():
        df[key] = df[key].map(translation.mappings).fillna(df[key])
        df.rename(columns={key: translation.name}, inplace=True)

    df.to_csv(output_path, index=False)
    print(f'output dataset loaded to {output_path}')


# By default, drop those with 90%+ missing values and only keep ASIA at discharge as target
# Also drop height/weight because there are a lot of missing values. Non-stochastic imputation will cause a huge artificial spike on specific values.
# Possible TODO: Replace height/weight with a BMI feature and one-hot encode based on low/healthy/high/unknown
def get_dataset_df(input_path, output_path, target_col='ASIA - Discharge', drop_cols=[
    'Anal Sensation - Admission', 
    'Anal Contraction - Admission', 
    'Family Income - Injury', 
    'Neurologic Category - Discharge',
    'Height - Admission',
    'Weight - Admission', 
    'Level of Injury - Discharge',
    'Occupation Code - Injury']):
    load_dataset(input_path, output_path)
    
    df = pd.read_csv(output_path)

    df.drop(drop_cols, axis=1, inplace=True)
    df = df[df[target_col] != 'Unknown']
    # Get rid of all unknown level of injury values and ASIA scores. This is crucial to SCI prognosis in practice.
    df = df[(df['Level of Injury - Admission'] != 'Unknown') & 
            (df['Level of Injury - Admission'] != 'C Unknown') & 
            (df['Level of Injury - Admission'] != 'T Unknown') & 
            (df['Level of Injury - Admission'] != 'L Unknown') & 
            (df['Level of Injury - Admission'] != 'S Unknown') &
            (df['ASIA - Admission'] != 'Unknown')]
    
    df = f1_categorical_transformations.transform_all(df)
    df.sort_values(by=['Injury Date'], inplace=True)

    print(f'Dataset shape: {df.shape}')
    return df

# Undo one-hot encoding and return "real life" features.
def get_practical_features(df):
    ml_features = df.columns.tolist()
    result = set()

    for ml_feature in ml_features:
        result.add(ml_feature.split('_')[0])
    
    return result

def get_train_test_split(df, target_col='ASIA - Discharge', injury_date_start=2006, drop_patients_who_worsened=False):
    df_local = df.copy()

    if drop_patients_who_worsened:
        orig_row_count = df_local.shape[0]
        
        df_local = df_local[
            (df_local['ASIA - Admission_A'] == 1) | 
            ((df_local['ASIA - Admission_B'] == 1) & (df_local[target_col] > 1)) |
            ((df_local['ASIA - Admission_C'] == 1) & (df_local[target_col] > 2)) |
            ((df_local['ASIA - Admission_D'] == 1) & (df_local[target_col] > 3)) |
            (df_local[target_col] == 5)]
        print(f'Patients who worsened = {orig_row_count - df_local.shape[0]} ({round(100 * (orig_row_count - df_local.shape[0]) / orig_row_count, 2)}%)')

    df_train = df_local[df_local['Injury Date'] < injury_date_start]
    df_test = df_local[df_local['Injury Date'] >= injury_date_start]

    df_train = df_train.drop(['Injury Date'], axis=1)
    df_test = df_test.drop(['Injury Date'], axis=1)

    train_x = df_train.drop([target_col], axis=1)
    train_y = df_train[target_col]

    test_x = df_test.drop([target_col], axis=1)
    test_y = df_test[target_col]

    train_x = train_x.reindex(sorted(train_x.columns), axis=1)
    test_x = test_x.reindex(sorted(test_x.columns), axis=1)
    
    print(f'{df_train.shape[0] / df_local.shape[0]} : {df_test.shape[0] / df_local.shape[0]} split for testing starting at injury date {injury_date_start}.')

    return train_x, train_y, test_x, test_y

if __name__ == '__main__':
    load_dataset('csvs/f1_public.csv', 'csvs/translated_dataset.csv')