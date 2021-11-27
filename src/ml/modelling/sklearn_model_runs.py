import sys
sys.path.append('..')
sys.path.append('../..')
import numpy as np
import argparse
import pickle
from data import dataset_loader
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score,recall_score,f1_score

def run_metrics(clf, train_x, train_y, test_x, test_y):
    """
    Print ML classifier metrics on train and test
    """
    accuracyTrain = clf.score(train_x, train_y)
    print(f'Accuracy on train set: {accuracyTrain}')
    
    accuracy = clf.score(test_x, test_y)
    print(f'Accuracy on test set: {accuracy}')

    precisionTrain = precision_score(train_y, clf.predict(train_x), average="macro")
    print(f'Precision on train set: {precisionTrain}')
    
    precision = precision_score(test_y, clf.predict(test_x), average="macro")
    print(f'Precision on test set: {precision}')

    recallTrain = recall_score(train_y, clf.predict(train_x), average="macro")
    print(f'Recall on train set: {recallTrain}')
    
    recall = recall_score(test_y, clf.predict(test_x), average="macro")
    print(f'Recall on test set: {recall}')
    
    f1Train = f1_score(train_y, clf.predict(train_x), average="macro")
    print(f'F1-Score on train set: {f1Train}')
    
    f1 = f1_score(test_y, clf.predict(test_x), average="macro")
    print(f'F1-Score on test set: {f1}')


def run_random_forest(train_x, train_y, test_x, test_y, num_trees):
    clf = RandomForestClassifier(n_estimators=num_trees)
    clf.fit(train_x, train_y)
    
    clf.inference_features = list(test_x.columns.values)

    print('Random Forest')
    run_metrics(clf, train_x, train_y, test_x, test_y)

    return clf

# Best model yet.
def run_elastic_net(train_x, train_y, test_x, test_y, penalty_type, iters, solver_name, l1_ratio_frac):
    clf = LogisticRegression(penalty=penalty_type, max_iter=iters, solver=solver_name, l1_ratio=l1_ratio_frac)
    clf.fit(train_x, train_y)

    clf.inference_features = list(test_x.columns.values)

    print('Elastic Net')
    run_metrics(clf, train_x, train_y, test_x, test_y)

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
    
    # Add model runs here.
    # clf = run_random_forest(train_x, train_y, test_x, test_y, num_trees=1000)
    clf = run_elastic_net(train_x, train_y, test_x, test_y, penalty_type='elasticnet', iters=200, solver_name='saga', l1_ratio_frac=0.9)

    # Save model.
    with open('pickles/model.pkl', 'wb') as f:
        pickle.dump(clf, f)

    # Explain best model.
    if args.interpret:
        from importance import run_importance
        run_importance(clf, train_x)

if __name__ == '__main__':
    main()