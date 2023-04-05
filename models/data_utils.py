import pandas as pd

def get_test_set():
    believable_by_few = pd.read_csv('../believable_by_few.csv', sep=',')
    believable_by_many = pd.read_csv('../believable_by_many.csv', sep=',')
    
    # print(believable_by_few.iloc[-50:])
    # print(believable_by_many.iloc[-50:])
    
    # print(pd.concat([believable_by_few.iloc[-50:], believable_by_many.iloc[-50:]], axis = 0))
    
    return believable_by_few.iloc[-50:], believable_by_many.iloc[-50:]

def eval_metrics(labels, targets):
    if len(labels) != len(targets):
        raise Exception("labels and targets must have the same length")
    
    true_pos = true_neg = false_pos = false_neg = 0
    
    for i, a in enumerate(labels):
        if a == 1 and targets[i] == 1:
            true_pos += 1
        elif a == 0 and targets[i] == 0:
            true_neg += 1
        elif a == 1 and targets[i] == 0:
            false_pos += 1
        else:   # a == 0 and targets[i] == 1
            false_neg += 1
    
    accuracy = (true_pos + true_neg) / len(labels)
    precision = true_pos / (true_pos + false_pos)
    recall = true_pos / (true_pos + false_neg)
    f1 = 2 * precision * recall / (precision + recall)
    
    print(f'accuracy: {accuracy}')
    print(f'precision: {precision}')
    print(f'recall: {recall}')
    print(f'f1 score: {f1}')
    
    return accuracy, precision, recall, f1

get_test_set()