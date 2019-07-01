#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 19-5-15 下午6:39
# @Author : ho-ho
# @Site :
# @File : testcd.py
# @Description:
# -------------------------------------------------------------------------------------
import pandas as pd
import jieba

# 准备数据
df_law = pd.read_csv("law.csv", encoding='utf-8')
df_law = df_law.dropna()  # drop掉空行

#df_eco = pd.read_csv("eco.csv", encoding='utf-8')
#df_eco = df_eco.dropna()

#df_psy = pd.read_csv("xinli.csv", encoding='utf-8')
#df_psy = df_psy.dropna()

#df_yao = pd.read_csv("yao.csv", encoding='utf-8')
#df_yao = df_yao.dropna()


law = df_law.content.values.tolist()[:1661] #276 1109
#eco = df_eco.content.values.tolist()[:1983]#330 1623
#psy = df_psy.content.values.tolist()[:1963]#327 1309
#yao = df_yao.content.values.tolist()[:1419]#236 947

# 去停用词
def preprocess_text(content_lines, sentences, category):
    for line in content_lines:
        try:
            sentences.append(str(category)+"\t"+"".join(line))
        except Exception as e:
            print(line)
            continue

# 生成训练数据
sentences = []

preprocess_text(law, sentences, '法学')
#preprocess_text(eco, sentences, '经济学')
#preprocess_text(psy, sentences, '心理学')
#preprocess_text(yao, sentences, '医学')

out = open('train_data_law.txt', 'w')
for sentence in sentences:
    out.write(sentence+"\n")
print("done!")