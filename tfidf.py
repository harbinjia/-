#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 19-4-6 下午7:16 
# @Author : ho-ho
# @Site :  
# @File : tfidf.py 
# @Software: PyCharm

"""
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ["I come to China to travel",
          "This is a car popular in China",
          "I love tea and Apple",
          "The work is to write some papers in science"]

vectorizer = CountVectorizer()
# print(vectorizer.fit_transform(corpus))  # 统计词频
# print(vectorizer.fit_transform(corpus).toarray())  # 词向量特征
# print(vectorizer.get_feature_names())  # 各个特征代表的词


# CountVectorizer+TFidfTransformer的组合
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
print(tfidf)  # 输出各个文本各个词的TF-IDF值

# 用TFidfVectorizer一步到位
tfidf2 = TfidfVectorizer()
re = tfidf2.fit_transform(corpus)
print(re)

import jieba
# 分词

with open('./nlp_text0.txt') as f:
    document = f.read()
    jieba.suggest_freq('沙瑞金', True)
    jieba.suggest_freq('易学习', True)
    jieba.suggest_freq('王大路', True)
    jieba.suggest_freq('京州', True)
    document_cut = jieba.cut(document)
    result = ' '.join(document_cut)
    with open('./nlp_text3.txt', 'w') as f2:
        f2.write(result)

f.close()
f2.close()
"""


import sys
sys.path.append("../")
import jieba
import jieba.posseg as pseg
from jieba import analyse
from sklearn.feature_extraction.text import TfidfVectorizer

jieba.suggest_freq('沙瑞金', True)
jieba.suggest_freq('易学习', True)
jieba.suggest_freq('王大路', True)
jieba.suggest_freq('京州', True)
jieba.suggest_freq('欧阳菁', True)
#加载停用词表
stop = [line.strip().encode('utf-8').decode('utf-8') for line in open('stopwords.txt').readlines() ]
'''#导入自定义词典  
jieba.load_userdict("userdict.txt")'''

# 读取文本
f = open('nlp_text0.txt')  # 打开原始文本，默认路径为python的安装路径
s = f.read()  # 读取文本

# 分词
segs = jieba.cut(s, cut_all=False)
#print u"[精确模式]: ", "  ".join(segs)
#s为需要分词的字符串；cut_all表示是否使用全模式

#分词并标注词性
segs = pseg.cut(s)

#写入文本
outputs = open('text2.txt','wb')
final = ''
for seg,flag in segs:
    #去停用词
    if seg not in stop:
       #去数词(m)和去字符串(x)
       if flag !='m' and flag !='x':
            #输出分词
            final =' '+ seg
            #输出分词带词性
            #final +=' '+ seg+'/'+flag
            outputs.write(final.encode())#将final内容写入text2中

outputs.close()
print('end')

with open('text2.txt') as f:
    res = f.read()
corpus = [res]
vector = TfidfVectorizer()
tfidf = vector.fit_transform(corpus)
# print(tfidf)
wordlist = vector.get_feature_names()
weightlist = tfidf.toarray()
for i in range(len(weightlist)):
    print("----第",i,"段文本的词语tf-idf权重----")
    for j in range(len(wordlist)):
        print(wordlist[j],weightlist[i][j])



'''
seg_list = jieba.cut("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作",cut_all=False)
seg_list = "/".join(seg_list)
print (seg_list)
'''

























