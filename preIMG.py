import cv2
import numpy as np

train_x = np.zeros((1,784))
train_x.shape
idx =0
for x in range(1,10001):
    input = cv2.imread(str(x)+'.png')
    his_input = np.array(cv2.cvtColor(input, cv2.COLOR_BGR2GRAY),int)

    img = np.array([])
    for i in range(28):
        for j in range(28):
            img = np.append(img,his_input[i,j])

    train_x = np.insert(train_x, idx, np.array(img), 0)
    idx=idx+1


for x in range(1,2001):
    input = cv2.imread('('+str(x)+').png')
    his_input = np.array(cv2.cvtColor(input, cv2.COLOR_BGR2GRAY),int)

    img = np.array([])
    for i in range(28):
        for j in range(28):
            img = np.append(img,his_input[i,j])

    train_x = np.insert(train_x, idx, np.array(img), 0)
    idx=idx+1

train_x = train_x[0:12000]
train_x.shape
train_x

train_label1 = np.ones((10000))
train_label2 = np.ones((2000))*2
train_label= np.hstack((train_label1,train_label2))

from sklearn.neural_network import MLPClassifier
mlp_model = MLPClassifier(hidden_layer_sizes=(50,30))
mlp_model.fit(train_x,train_label)

test_x = np.zeros((1,784))
idx =0
for x in range(1,351):
    input = cv2.imread('test ('+str(x)+').png')
    his_input = np.array(cv2.cvtColor(input, cv2.COLOR_BGR2GRAY),int)

    img = np.array([])
    for i in range(28):
        for j in range(28):
            img = np.append(img,his_input[i,j])

    test_x = np.insert(test_x, idx, np.array(img), 0)
    idx=idx+1
test_x.shape
test_x
for x in range(351,1516):
    input = cv2.imread('test ('+str(x)+').png')
    his_input = np.array(cv2.cvtColor(input, cv2.COLOR_BGR2GRAY),int)

    img = np.array([])
    for i in range(28):
        for j in range(28):
            img = np.append(img,his_input[i,j])

    test_x = np.insert(test_x, idx, np.array(img), 0)
    idx=idx+1

test_x = test_x[0:1515]
test_x.shape
test_x
test_label1 = np.ones((350))*2
test_label2 = np.ones((1166))
test_label= np.hstack((test_label1,test_label2))

test_label= np.hstack((test_label1,test_label2))
test_label.shape

test_label= test_label[0:1515]
test_label.shape

print(mlp_model.score(test_x, test_label))

print(mlp_model.predict(test_x))
