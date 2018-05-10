import tensorflow as tf
import numpy as np

# 计算图的其他操作

sess = tf.Session()
#div()函数返回值的数据类型与输入数据类型一致
print(sess.run(tf.div(3, 4)))

#truediv()函数会将计算结果强制转换为浮点数类型
print(sess.run(tf.truediv(3, 4)))

#floordiv()函数，会将计算结果向下取整
print(sess.run(tf.floordiv(5, 4)))

#mod()取模运算，返回除法的余数
print(sess.run(tf.mod(22.0, 5.0)))

#通过cross()函数计算两个张量级的点积。只为三维向量定义。
print(sess.run(tf.cross([1., 0., 0.], [0., 1., 0.])))

# 组合预处理函数生成自定义函数
print(sess.run(tf.div(tf.sin(3.1416/4.), tf.cos(3.1416/4.))))

# 延伸学习
#创建一个自定义二次多项式函数，3x^2-x+10
def custom_polynomial(value):
    return(tf.subtract(3 * tf.square(value),value)+10)
print(sess.run(custom_polynomial(11)))