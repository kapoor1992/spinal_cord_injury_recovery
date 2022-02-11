import sys
sys.path.append('..')
sys.path.append('../..')
import numpy as np
import argparse
import pickle
from data import dataset_loader, metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


def run_random_forest(train_x, train_y, test_x, test_y, train_matches_dict, test_matches_dict, num_trees):
    clf = RandomForestClassifier(n_estimators=num_trees)
    clf.fit(train_x, train_y)
    
    clf.inference_features = list(test_x.columns.values)

    print('-----')
    print('Random Forest')
    metrics.run_metrics(clf, train_x, train_y, test_x, test_y, train_matches_dict, test_matches_dict)

    return clf

# Best model yet.
def run_elastic_net(train_x, train_y, test_x, test_y, train_matches_dict, test_matches_dict, penalty_type, iters, solver_name, l1_ratio_frac):
    clf = LogisticRegression(penalty=penalty_type, max_iter=iters, solver=solver_name, l1_ratio=l1_ratio_frac)
    clf.fit(train_x, train_y)

    clf.inference_features = list(test_x.columns.values)

    print('-----')
    print('Elastic Net')
    metrics.run_metrics(clf, train_x, train_y, test_x, test_y, train_matches_dict, test_matches_dict)

    return clf


def main():
    # Only do these lines once.
    parser = argparse.ArgumentParser()
    parser.add_argument('--interpret', action='store_true')
    args = parser.parse_args()

    # Same with these.
    np.random.seed(2)
    df = dataset_loader.get_dataset_df('../data/csvs/f1_public.csv', '../data/csvs/translated_dataset.csv')
    train_x, train_y, test_x, test_y = dataset_loader.get_train_test_split(df)

    print('-----')
    print('ASIA matches between admission and discharge in training set:')
    train_matches_dict = metrics.display_matches_dict(train_x, train_y)

    print('-----')
    print('ASIA matches between admission and discharge in testing set:')
    test_matches_dict = metrics.display_matches_dict(test_x, test_y)

    print('-----')
    print(f'Total samples:          {train_y.shape[0] + test_y.shape[0]}') # 20,790
    print(f'Total training samples: {train_y.shape[0]}') # 18,737
    print(f'Total testing samples:  {test_y.shape[0]}') # 2,053
    print(f'Total ML features:      {train_x.shape[1]}') # 53
    print(f'Total "real" features:  {len(dataset_loader.get_practical_features(train_x))}') # 18
    print('-----')

    # Add model runs here.
    # clf = run_random_forest(train_x, train_y, test_x, test_y, train_matches_dict, test_matches_dict, num_trees=1000)
    clf = run_elastic_net(train_x, train_y, test_x, test_y, train_matches_dict, test_matches_dict, 
                          penalty_type='elasticnet', iters=200, solver_name='saga', l1_ratio_frac=0.9)

    # Save model.
    with open('pickles/model.pkl', 'wb') as f:
        pickle.dump(clf, f)

    # Explain best model.
    if args.interpret:
        from importance import run_importance
        run_importance(clf, train_x)

if __name__ == '__main__':
    main()