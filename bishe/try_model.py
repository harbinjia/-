#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 19-5-5 下午4:20 
# @Author : ho-ho
# @Site :  
# @File : try_model.py 
# @Description: 
# -------------------------------------------------------------------------------------

import jieba
import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score,f1_score
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score

# 准备数据
df_law = pd.read_csv("data/law.csv", encoding='utf-8')
df_law = df_law.dropna()  # drop掉空行

df_eco = pd.read_csv("data/eco.csv", encoding='utf-8')
df_eco = df_eco.dropna()

df_psy = pd.read_csv("data/xinli.csv", encoding='utf-8')
df_psy = df_psy.dropna()

df_yao = pd.read_csv("data/yao.csv", encoding='utf-8')
df_yao = df_yao.dropna()

law = df_law.content.values.tolist()[:1661]
eco = df_eco.content.values.tolist()[:1983]
psy = df_psy.content.values.tolist()[:1963]
yao = df_yao.content.values.tolist()[:1419]

# 引入停用词
stopwords = pd.read_csv("data/stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'], encoding='utf-8')
stopwords = stopwords['stopword'].values

# 去停用词
def preprocess_text(content_lines, sentences, category):
    for line in content_lines:
        try:
            segs = jieba.lcut(line)
            segs = filter(lambda x: x not in stopwords, segs)  # 去停用词
            segs = filter(lambda x: len(x) > 1, segs)  # 去长度小于１
            sentences.append((" ".join(segs), category))
        except Exception as e:
            print(line)
            continue

# 生成训练数据
sentences = []
preprocess_text(law, sentences, '--法学--')
preprocess_text(eco, sentences, '--经济--')
preprocess_text(psy, sentences, '--心理学--')
preprocess_text(yao, sentences, '--医学--')

# 打乱顺序
# random.shuffle(sentences)

# 生成训练集和测试集，比例为4:1
x, y = zip(*sentences)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
#print(len(x_test))

vec = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), max_features=7000)
X_train = vec.fit_transform(x_train)
X_test = vec.transform(x_test)
# 建立模型,使用多项式朴素贝叶斯
bys = MultinomialNB()
TT = bys.fit(X_train, y_train)
# 预测
y_predict = TT.predict(X_test)
# 五折交叉验证
scores = cross_val_score(bys, X_test, y_test, cv=5, scoring="accuracy")
# print(scores)
print("NB_Accuracy:%.3f" % scores.mean())
print("NB_classification_report:\n", classification_report(y_predict, y_test))

# 建立支持向量机模型
svm = LinearSVC()
ss = svm.fit(X_train, y_train)
y_pre = ss.predict(X_test)
sco = cross_val_score(svm, X_test, y_test, cv=5, scoring="accuracy")
print("SVM_Accuracy:%.3f" % sco.mean())
print("SVM_classification_report:\n", classification_report(y_pre,y_test))


'''
print(x_train[0:1])
print(y_train[0:1])
cls = LinearSVC()
cls.fit(x_train,y_train)
print("%.2f" % cls.score(x_test,y_test))
'''
"""
# 特征抽取，词袋模型，用CountVectorizer,只考虑词汇出现在文本中的频率
vec = CountVectorizer(
    analyzer='word',  # tokenise by character ngrams
    ngram_range=(1,4),
    max_features=7000,  # keep the most common 1000 ngrams
)
# 将训练数据转为词袋模型
vec.fit(x_train)

def get_features(x):
    vec.transform(x)

# 用多项式分布朴素贝斯分类器训练
classifier = MultinomialNB()
classifier.fit(vec.transform(x_train), y_train)
# 准确率
test_score = classifier.score(vec.transform(x_test), y_test)
print("Score on test set:{:.2f}".format(test_score))

# 五折分层交叉验证
def stratifiedkfold_cv(x, y, clf_class, **kwargs):
    stratifiedk_fold = StratifiedKFold(n_splits=5, shuffle=False)

    y_pred = y[:]
    for train_index, test_index in stratifiedk_fold.split(x, y):
        X_train, X_test = x[train_index], x[test_index]
        y_train = y[train_index]
        clf = clf_class(**kwargs)
        clf.fit(X_train, y_train)
        y_pred[test_index] = clf.predict(X_test)
    return y_pred

NB = MultinomialNB
pre = precision_score(y, stratifiedkfold_cv(vec.transform(x), np.array(y), NB), average='macro')
print("Pre score on NB:{:.2f}".format(pre))
print(recall_score(y, stratifiedkfold_cv(vec.transform(x), np.array(y), NB)))
# y_pred是预测标签
print(classification_report(y_true=y_true, y_pred=y_pred))
"""
'''
# 朴素贝叶斯文本分类器

class TextClassifier():

    def __init__(self, classifier=MultinomialNB()):
        self.classifier = classifier
        #self.vectorizer = CountVectorizer(analyzer='word',ngram_range=(1,4), stop_words='english', max_features=7000)
        self.vectorizer = TfidfVectorizer(analyzer='word', max_features=7000)
    # 生成向量
    def features(self, X):
        return self.vectorizer.transform(X)
    # 训练
    def fit(self, X, y):
        self.vectorizer.fit(X)
        self.classifier.fit(self.features(X), y)
    # 预测
    def predict(self, x):
        return self.classifier.predict(self.features([x]))
    # AUC值
    def score(self, X, y):
        return self.classifier.score(self.features(X), y)

# 预测，输出正确率
text_classifier = TextClassifier()
text_classifier.fit(x_train, y_train)
'''
'''
print(text_classifier.predict('大学生 实习 是 为了 学习 专业 技能 ， 琐碎 工作 不值得 ， 这种 观点 对吗 ？'))
print(text_classifier.predict('与 人 产生 纠纷 怎么 处理'))
print(text_classifier.predict('可以 推荐 一些 炒股 技巧 吗 ？'))
print(text_classifier.predict('我 认为 西方 的 法 应 理解 为 ： 理想法 、 应然法 、 客观法 ， 为什么 在 测验 中 不 把 “ 法 ” 理解 为 客观法 ？'))
print(text_classifier.score(x_test, y_test))
'''
'''
class TextClassifier():

    def __init__(self, classifier=LinearSVC()):
        self.classifier = classifier
        self.vectorizer = TfidfVectorizer(analyzer='word', max_features=7000)

    def features(self, X):
        return self.vectorizer.transform(X)

    def fit(self, X, y):
        self.vectorizer.fit(X)
        self.classifier.fit(self.features(X), y)

    def predict(self, x):
        return self.classifier.predict(self.features([x]))

    def score(self, X, y):
        return self.classifier.score(self.features(X), y)

text_classifier = TextClassifier()
text_classifier.fit(x_train, y_train)
'''
'''print(text_classifier.predict('大学生 实习 是 为了 学习 专业 技能 ， 琐碎 工作 不值得 ， 这种 观点 对吗 ？'))
print(text_classifier.predict('可以 推荐 一些 炒股 技巧 吗 ？'))
print(text_classifier.predict('我 认为 西方 的 法 应 理解 为 ： 理想法 、 应然法 、 客观法 ， 为什么 在 测验 中 不 把 “ 法 ” 理解 为 客观法 '))
print(text_classifier.predict('与 人 产生 纠纷 怎么 处理'))
print(text_classifier.score(x_test, y_test))
'''
