import tensorflow as tf
import numpy as np

# 实现激励函数

sess = tf.Session()
# 显式调用内建激励函数
# 1.整流线性单元（Rectifier linear unit，ReLU）神经网络常用非线性函数
# 函数为max（0，x）连续但不平滑。
print(sess.run(tf.nn.relu([-3., 3., 10.])))

#2.为限制ReLU的线性增长部分，会在min（）函数中嵌入max（0，x），其在tf中的实现成为ReLU6，表示
# min(max(0,x),6),这个是hard-sigmoid函数的变种，计算运行速度快，解决梯度消失（无线趋于0）
print(sess.run(tf.nn.relu6([-3., 3., 10.])))

# 3.sigmoid函数是最常用的连续、平滑的激励函数。
# 也被称作逻辑函数（logistic函数），表示为1/(1+exp(-x))。
# sigmoid函数用于在机器学习训练过程中反向传播项趋近于0，因此不怎么使用。
print(sess.run(tf.nn.sigmoid(-1., 0., 2)))#此处有错

# 自定义设计激励函数

