from sklearn.metrics import precision_score, recall_score, f1_score

def get_matches_dict(df_x, df_y):
    # List values are (<key_equivalent_in_target_variable>, <matches>, <mismatches>)
    matches_dict = {
        'A': [1, 0, 0], 
        'B': [2, 0, 0], 
        'C': [3, 0, 0], 
        'D': [4, 0, 0]
    }
    
    for i, row in df_x.iterrows():
        for k, v in matches_dict.items():
            if row[f'ASIA - Admission_{k}'] == 1:
                if df_y[i] == v[0]:
                    v[1] += 1
                else:
                    v[2] += 1
                break
    
    return matches_dict

def display_matches_dict(df_x=None, df_y=None, matches_dict=None, only_rate=False):
    '''
    Must provide one of df_x/df_y OR matches_dict
    '''
    if matches_dict is None:
        matches_dict = get_matches_dict(df_x, df_y)

    for k, v in matches_dict.items():
        if not only_rate:
            print(f'ASIA {k} Matches:    {v[1]}')
            print(f'ASIA {k} Misses:     {v[2]}')
        print(f'ASIA {k} Match Rate: {round(v[1] / (v[1] + v[2]), 4)}')
    
    return matches_dict

def run_metrics(clf, train_x, train_y, test_x, test_y):
    """
    Print ML classifier metrics on train and test
    """
    accuracyTrain = clf.score(train_x, train_y)
    print(f'Accuracy on train set: {accuracyTrain}')

    train_prediction = clf.predict(train_x)
    test_prediction = clf.predict(test_x)
    
    accuracy = clf.score(test_x, test_y)
    print(f'Accuracy on test set: {accuracy}')

    precisionTrain = precision_score(train_y, train_prediction, average="macro")
    print(f'Precision on train set: {precisionTrain}')
    
    precision = precision_score(test_y, test_prediction, average="macro")
    print(f'Precision on test set: {precision}')

    recallTrain = recall_score(train_y, train_prediction, average="macro")
    print(f'Recall on train set: {recallTrain}')
    
    recall = recall_score(test_y, test_prediction, average="macro")
    print(f'Recall on test set: {recall}')
    
    f1Train = f1_score(train_y, train_prediction, average="macro")
    print(f'F1-Score on train set: {f1Train}')
    
    f1 = f1_score(test_y, test_prediction, average="macro")
    print(f'F1-Score on test set: {f1}')
