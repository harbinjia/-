#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 19-5-5 下午1:02 
# @Author : ho-ho
# @Site :  
# @File : createfile.py 
# @Description: 
# -------------------------------------------------------------------------------------

import pandas as pd
import random
import jieba

import pandas as pd
import random
"""
df_zhe = pd.read_csv("xinli.csv", encoding='utf-8',error_bad_lines=False)
df_zhe = df_zhe.dropna()

# 获取数据
#law = df_zhe.content.values.tolist()[:2184] # vc361t1453　
#eco = df_zhe.content.values.tolist()[:2145]  # vc357t1429
psy = df_zhe.content.values.tolist()[:2386] # vc397t1589　　2371
#zhe = df_zhe.content.values.tolist()[:2302] #2246  374  1498　　2300

# 引入停用词
stopwords = pd.read_csv("stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                        encoding='utf-8')
stopwords = stopwords['stopword'].values

# 去停用词
def preprocess_text(content_lines, sentences, category):
    for line in content_lines:
        try:
            segs = jieba.lcut(line)
            segs = filter(lambda x: x not in stopwords, segs)
            segs = list(filter(lambda x: len(x) > 1, segs)) # 去除长度小于１

            if segs != "":
                sentences.append("__label__"+str(category)+" , "+" ".join(segs))
        except Exception as e:
            print(line)
            continue

#生成训练数据
sentences = []
#preprocess_text(eco, sentences, '经济类')
#preprocess_text(law, sentences, '政治类')
preprocess_text(psy, sentences, '心理学类')
#preprocess_text(zhe, sentences, '哲学类')
# random.shuffle(sentences)

print("writing data to fasttext format...")
out = open('try_xinli.txt', 'w')
for sentence in sentences:
    out.write(sentence+"\n")
print("done!")
"""

df_zhe = pd.read_csv("law.csv", encoding='utf-8',error_bad_lines=False)
df_zhe = df_zhe.dropna()

# 获取数据
law = df_zhe.content.values.tolist()[:2184]#vc364t1456
#eco = df_eco.content.values.tolist()[:2145]vc357t1431
#psy = df_psy.content.values.tolist()[:2383]vc397t1589
#zhe = df_zhe.content.values.tolist()[:2302] 2246  374  1498
"""
# 引入停用词
stopwords = pd.read_csv("stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                        encoding='utf-8')
stopwords = stopwords['stopword'].values
"""
# 去停用词
def preprocess_text(content_lines, sentences, category):
    for line in content_lines:
        try:
            sentences.append(str(category)+"\t"+"".join(line))
        except Exception as e:
            print(line)
            continue

#生成训练数据
sentences = []
#preprocess_text(psy, sentences, '心理学类')
preprocess_text(law, sentences, '哲学类')
# random.shuffle(sentences)

print("writing data to fasttext format...")
out = open('train_new_zhe.txt', 'w')
for sentence in sentences:
    out.write(sentence+"\n")
print("done!")