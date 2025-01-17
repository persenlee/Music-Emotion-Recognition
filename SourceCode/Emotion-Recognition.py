"""
@author: Danyal

The following code classifies piece of music as one of 
the four emotions mentioned in the document
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv('/root/Music-Emotion-Recognition/Emotion_features_std.csv')
feature = data.iloc[:, 4:]
featureName = list(feature)
color = ['red' if l==1 else 'green' if l==2 else 'blue' if l==3 else 'orange' for l in data['label']]

for name in featureName:
    feature[name] = (feature[name]-feature[name].min())/(feature[name].max()-feature[name].min())

plt.style.use('ggplot')

array = np.array(data)

features = feature.values
labels = data.iloc[:, 3].dropna()
test_size = 0.20
random_seed = 7

# 随机划分训练集和测试集 
train_d, test_d, train_l, test_l = train_test_split(features, labels, test_size=test_size, random_state=random_seed)

# result = []
# xlabel = [i for i in range(1, 11)]
# for neighbors in range(1, 11):
#     kNN = KNeighborsClassifier(n_neighbors=neighbors)
#     kNN.fit(train_d, train_l)
#     prediction = kNN.predict(test_d)
#     result.append(accuracy_score(prediction, test_l)*100)

# print(result)

# plt.figure(figsize=(10, 10))
# plt.xlabel('kNN Neighbors for k=1,2...20')
# plt.ylabel('Accuracy Score')
# plt.title('kNN Classifier Results')
# plt.ylim(0, 100)
# plt.ylim = [0, 100]
# plt.xlim(0, xlabel[len(xlabel)-1]+1)
# plt.xlim = [0, xlabel[len(xlabel)-1]+1]
# plt.plot(xlabel, result)
# plt.savefig('1-fold 10NN Result.png')
# plt.show()

kNN = KNeighborsClassifier(n_neighbors=2)
kNN.fit(train_d, train_l)

inputData = pd.read_csv('/root/Music-Emotion-Recognition/Data/Emotion_features_std.csv')
inputFeature = inputData.iloc[:, 2:]
predict = kNN.predict(inputFeature.values)
print(predict)