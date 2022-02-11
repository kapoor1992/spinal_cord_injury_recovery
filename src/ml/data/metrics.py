from sklearn.metrics import precision_score, recall_score, f1_score

def get_matches_dict(df_x, df_y):
    # List values are (<key_equivalent_in_target_variable>, <matches>, <mismatches>)
    matches_dict = {
        'A': [1, 0, 0], 
        'B': [2, 0, 0], 
        'C': [3, 0, 0], 
        'D': [4, 0, 0]
    }
    
    df_x_copy = df_x.copy()
    df_x_copy.reset_index(drop=True, inplace=True)
    
    df_y_copy = df_y.copy()
    df_y_copy.reset_index(drop=True, inplace=True)

    for i, row in df_x_copy.iterrows():
        for k, v in matches_dict.items():
            if row[f'ASIA - Admission_{k}'] == 1:
                if df_y_copy[i] == v[0]:
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

def get_admission_to_correct_dict(df_x, df_y, predictions):
    '''
    Returns a dictionary where the admission ASIA score is mapped to the number of correct predictions.
    '''
    # List values are (<key_equivalent_in_target_variable>, <correct>, <incorrect>)
    admission_to_correct_dict = {
        'A': [1, 0, 0], 
        'B': [2, 0, 0], 
        'C': [3, 0, 0], 
        'D': [4, 0, 0]
    }
    
    df_x_copy = df_x.copy()
    df_x_copy.reset_index(drop=True, inplace=True)
    
    df_y_copy = df_y.copy()
    df_y_copy.reset_index(drop=True, inplace=True)

    for i, row in df_x_copy.iterrows():
        for k, v in admission_to_correct_dict.items():
            if row[f'ASIA - Admission_{k}'] == 1:
                if df_y_copy[i] == predictions[i]:
                    v[1] += 1
                else:
                    v[2] += 1
                break
    
    return admission_to_correct_dict

def display_admission_to_correct_dict(df_x=None, df_y=None, predictions=None, admission_to_correct_dict=None, only_rate=False):
    '''
    Must provide one of df_x/df_y/predictions OR admission_to_correct_dict
    '''
    if admission_to_correct_dict is None:
        admission_to_correct_dict = get_admission_to_correct_dict(df_x, df_y, predictions)

    for k, v in admission_to_correct_dict.items():
        if not only_rate:
            print(f'Admission ASIA {k} Correct:      {v[1]}')
            print(f'Admission ASIA {k} Wrong:        {v[2]}')
        print(f'Admission ASIA {k} Correct Rate: {round(v[1] / (v[1] + v[2]), 4)}')
    
    return admission_to_correct_dict

def run_metrics(clf, train_x, train_y, test_x, test_y, train_matches_dict, test_matches_dict):
    """
    Print ML classifier metrics on train and test
    """
    accuracyTrain = clf.score(train_x, train_y)
    print(f'Accuracy on train set: {accuracyTrain}')

    train_predictions = clf.predict(train_x)
    test_predictions = clf.predict(test_x)
    
    accuracy = clf.score(test_x, test_y)
    print(f'Accuracy on test set: {accuracy}')

    precisionTrain = precision_score(train_y, train_predictions, average="macro")
    print(f'Precision on train set: {precisionTrain}')
    
    precision = precision_score(test_y, test_predictions, average="macro")
    print(f'Precision on test set: {precision}')

    recallTrain = recall_score(train_y, train_predictions, average="macro")
    print(f'Recall on train set: {recallTrain}')
    
    recall = recall_score(test_y, test_predictions, average="macro")
    print(f'Recall on test set: {recall}')
    
    f1Train = f1_score(train_y, train_predictions, average="macro")
    print(f'F1-Score on train set: {f1Train}')
    
    f1 = f1_score(test_y, test_predictions, average="macro")
    print(f'F1-Score on test set: {f1}')

    print('-----')
    print('Admission ASIA to correct prediction results (train set):')
    display_admission_to_correct_dict(train_x, train_y, train_predictions)
    
    print('-----')
    print('Admission ASIA to correct prediction results (test set):')
    display_admission_to_correct_dict(test_x, test_y, test_predictions)
