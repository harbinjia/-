#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 19-5-3 下午7:37 
# @Author : ho-ho
# @Site :  
# @File : modelNB.py 
# @Description: 
# -------------------------------------------------------------------------------------

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC


class TextClassifier():

    def __init__(self, classifier=LinearSVC()):
        self.cls = classifier
        self.vect = TfidfVectorizer(analyzer='word', max_features=7000)

    # 生成向量
    def features(self, X):
        return self.vect.transform(X)

    # 训练
    def fit(self, X, y):
        self.vect.fit(X)
        self.cls.fit(self.features(X), y)

    # 预测
    def predict(self, x):
        return self.cls.predict(self.features([x]))

    # 准确率
    def score(self, X, y):
        return self.cls.score(self.features(X), y)
