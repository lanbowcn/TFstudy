import tensorflow as tf
import numpy as np
# 使用占位符和变量
# 创建一个张量，需要将其赋值给一个变量或者占位符，tf才会将其增加到计算图

# 变量是TF机器学习算法的参数，tf维护（调整）这些变量的状态来优化机器学习算法

# 占位符是tf的对象，用于输入输出数据的格式，允许传入指定类型和形状的数据，
# 并依赖于计算图的计算结果，比如，期望的计算结果

# 变量
# tf中，使用tf.Variable()函数创建变量，具体过程是，输入一个张量，返回一个变量
# 声明变量后需要初始化变量。
# 创建变量并初始化
my_var=tf.Variable(tf.zeros([2,3]))
sess = tf.Session()
initialize_op = tf.global_variables_initializer()
sess.run(initialize_op)

# 占位符
# 占位符仅仅声明数据位置，用于传入数据到计算图。
# 占位符通过会话的feed_dict参数获取数据。计算图中使用占位符，
# 必须在其上执行至少一个操作

# 初始化计算图，声明一个占位符x，定义y为x的identity操作。
# identity操作返回占位符传入数据的本身
sess2 = tf.Session()#定义会话
x = tf.placeholder(tf.float32,shape = [2,2])
y = tf.identity(x)#定义为x的identity操作
x_vals = np.random.rand(2,2)
sess2.run(y, feed_dict={x:x_vals})#将x_vals的值传入x这个tensor