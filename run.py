#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 19-4-30 下午8:27 
# @Author : ho-ho
# @Site :  
# @File : run.py 
# @Description: 
# -------------------------------------------------------------------------------------


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import *
from test import Ui_Form
import sys
import numpy as np
from bishe.modelNB import TextClassifier
import jieba
from jieba.analyse import *
import pandas as pd
import random
from sklearn.model_selection import train_test_split


df_law = pd.read_csv("bishe/data/law.csv", encoding='utf-8')
df_law = df_law.dropna()  # drop掉空行

df_eco = pd.read_csv("bishe/data/eco.csv", encoding='utf-8')
df_eco = df_eco.dropna()

df_psy = pd.read_csv("bishe/data/xinli.csv", encoding='utf-8')
df_psy = df_psy.dropna()

df_yao = pd.read_csv("bishe/data/yao.csv", encoding='utf-8')
df_yao = df_yao.dropna()

law = df_law.content.values.tolist()[:1661]
eco = df_eco.content.values.tolist()[:1983]
psy = df_psy.content.values.tolist()[:1963]
yao = df_yao.content.values.tolist()[:1419]

# 引入停用词
stopwords = pd.read_csv("bishe/data/stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                        encoding='utf-8')
stopwords = stopwords['stopword'].values

# 去停用词,结巴分词
# 定义分词和打标签函数preprocess_text
# 参数content_lines即为上面转换的list
# 参数sentences是定义的空list，用来储存打标签之后的数据
# 参数category 是类型标签
def preprocess_text(content_lines, sentences, category):
    for line in content_lines:
        try:
            segs = jieba.lcut(line)
            segs = filter(lambda x: len(x) > 1, segs)  # 去除长度小于１
            segs = filter(lambda x: x not in stopwords, segs)
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

class mywindow(QWidget, Ui_Form):

    kk = []  #保存测试文本
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    def do_show(self,event):
        '''显示对话框返回值'''
        QMessageBox.about(self, "使用说明", "１、选择测试文件 弹出文件选择框，选择即可选择测试文件。\n２、点击查询按钮 点击后可看到测试文件的关键词和类别。\n３、点击清空按钮 点击后可清空结果显示框的内容。")

    def choose(self):
        fname,ok = QFileDialog.getOpenFileName(self, "打开文件", "./bishe/ceshi", "Txt(*.txt)")
        if ok:
            _f = open(fname,'r')
            with _f:
                data = _f.read()
                self.kk.append(data)
                self.result.append("测试文本：\n"+data+"\n===========")

    def select(self):
        dat = self.kk
        text = " ".join(jieba.lcut(str(dat)))
        #print(text)
        core = []
        for keyword,weight in extract_tags(text, topK=3, withWeight=True):
            #print('%s' % keyword)
            core.append(keyword)
        self.kk = []
        # 预测
        text_classifier = TextClassifier()
        text_classifier.fit(x_train, y_train)
        target = text_classifier.predict(text)
        self.result.append('关键词：' + core[0]+' '+core[1]+' '+core[2])
        self.result.append('类别:' + target[0]+'\n===========\n')

if __name__ == '__main__':
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        myWin = mywindow()
        myWin.show()
        sys.exit(app.exec_())
