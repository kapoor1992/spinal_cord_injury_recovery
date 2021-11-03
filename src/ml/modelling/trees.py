import sys
sys.path.append('..')
import numpy as np
from data import dataset_loader
from sklearn.ensemble import RandomForestClassifier

def main():
    df_x, df_y = dataset_loader.get_dataset_df_x_y('../data/csvs/f1_public.csv', '../data/csvs/translated_dataset.csv')
    
    train_ct = int(df_x.shape[0] * 0.9)
    train_x, train_y, test_x, test_y = df_x[:train_ct], df_y[:train_ct], df_x[train_ct:], df_y[train_ct:]
    
    clf = RandomForestClassifier(n_estimators = 1000)
    clf.fit(train_x.to_numpy(), train_y.to_numpy())
    
    accuracy = clf.score(test_x, test_y)
    print(accuracy)

if __name__ == '__main__':
    np.random.seed(2)
    main()