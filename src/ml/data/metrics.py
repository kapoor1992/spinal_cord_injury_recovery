from sklearn.metrics import precision_score, recall_score, f1_score

def run_metrics(clf, train_x, train_y, test_x, test_y):
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
