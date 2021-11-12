import sys
sys.path.append('..')
import numpy as np
import pickle
from data import dataset_loader
from sklearn.ensemble import RandomForestClassifier

def run_random_forest(train_x, train_y, test_x, test_y, num_trees):
    clf = RandomForestClassifier(n_estimators=num_trees)
    clf.fit(train_x, train_y)
    
    clf.inference_features = list(test_x.columns.values)

    with open('pickles/random_forest.pkl', 'wb') as f:
        pickle.dump(clf, f)
    
    accuracy = clf.score(test_x, test_y)
    print(f'Accuracy on test set: {accuracy}')


def main():
    # Only do these lines once.
    np.random.seed(2)
    df = dataset_loader.get_dataset_df('../data/csvs/f1_public.csv', '../data/csvs/translated_dataset.csv')
    train_x, train_y, test_x, test_y = dataset_loader.get_train_test_split(df)
    
    # Add model runs here.
    run_random_forest(train_x, train_y, test_x, test_y, num_trees=1000)
    

if __name__ == '__main__':
    main()