该项目基于python3+anaconda+tensorflow1.15＋pyqt5配置环境
首先、利用获取数据集。利用selenium模拟浏览器收集"中国大学MOOC"平台讨论区问题，经过数据清洗得到七千条数据。见文件bishe/mooczhua.py
其次、模型对比。使用三种模型：支持向量机，朴素贝叶斯，卷积神经网络。运用在该数据集上，经过试验在支持向量机模型上表现略优。见try_model.py可得朴素贝叶斯和支持向量机实验数据，在终端run runCNN.py train和run runnCNN.py test可得在CNN上的实验数据。
最后基于支持向量机模型搭建简易的文本类别预测系统。运行run.py可见文本分类系统。
