import sys
sys.path.append('..')
sys.path.append('../..')
import numpy as np
import argparse
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

    return clf, accuracy


def main():
    # Only do these lines once.
    parser = argparse.ArgumentParser()
    parser.add_argument('--interpret', action='store_true')
    args = parser.parse_args()

    np.random.seed(2)
    df = dataset_loader.get_dataset_df('../data/csvs/f1_public.csv', '../data/csvs/translated_dataset.csv')
    train_x, train_y, test_x, test_y = dataset_loader.get_train_test_split(df)
    
    # Add model runs here.
    clf, _ = run_random_forest(train_x, train_y, test_x, test_y, num_trees=1000)

    # Explain best model.
    if args.interpret:
        from importance import run_importance
        run_importance(clf, train_x)

if __name__ == '__main__':
    main()