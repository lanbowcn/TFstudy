import tensorflow as tf
import numpy as np
sess = tf.Session()

#np创建2D图像，4x4像素图片
x_shape = [1,4,4,1]#四维：图片数量、高度、宽度、颜色通道
x_val = np.random.uniform(size = x_shape)

# 创建占位符
x_data=tf.placeholder(tf.float32,shape=x_shape)

# 使用滑动窗口，使用TF内建函数conv2d（）进行卷积2x2
my_filter = tf.constant(0.25,shape=[2,2,1,1])
my_strides = [1,2,2,1]
mov_avg_layer = tf.nn.conv2d(x_data,my_filter,my_strides,padding='SAME',name='Moving_Avg_Window')

