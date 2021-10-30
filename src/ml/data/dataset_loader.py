import sys
sys.path.append('..')
import pandas as pd
import data.utils.f1_feature_translations as f1_feature_translations
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

if __name__ == '__main__':
    load_dataset('csvs/f1_public.csv', 'csvs/translated_dataset.csv')