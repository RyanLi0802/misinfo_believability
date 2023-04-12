import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import pandas as pd

import data_utils
from two_layer_nn import Net


few_train, many_train = data_utils.get_train_set()
print(few_train.shape[0], many_train.shape[0])

train_data = pd.concat([few_train, many_train], axis = 0)
train_targets = [0] * few_train.shape[0] + [1] * many_train.shape[0]

features = data_utils.extract_features(train_data)
print(train_data.shape)
print(features.shape)


input_size = features.shape[1]
hidden_size = 50
output_size = 2
epoch = 50

model = Net(input_size, hidden_size, output_size)
print(model.parameters())
optimizer = torch.optim.Adam(model.parameters(), lr=0.005)

model.train()
# model.double()

for i in range(epoch):
    # total_loss = 0
    optimizer.zero_grad()
    x = torch.from_numpy(features).float()
    logits = model(x)
    loss = F.cross_entropy(logits, torch.tensor(train_targets))
    # print(logits, train_targets[idx], loss)
    loss.backward()
    optimizer.step()
    print(f'epoch {i} training loss: {loss}')
    # predictions = torch.argmax(logits, dim=-1)
    # data_utils.eval_metrics(predictions, train_targets)
print("training complete!")


# evaluate
model.eval()
few_test, many_test = data_utils.get_test_set()
test_data = pd.concat([few_test, many_test], axis = 0)

test_targets = [0] * few_test.shape[0] + [1] * many_test.shape[0]
test_features = data_utils.extract_features(test_data)

scores = model(torch.from_numpy(test_features).float())
predictions = torch.argmax(scores, dim=-1)
data_utils.eval_metrics(predictions, test_targets)