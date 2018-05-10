import tensorflow as tf
# 声明张量

#1 固定张量
zero_tsr = tf.zeros([row_dim,col_dim])#创建指定维度的零张量
ones_tsr = tf.ones([row_dim,col_dim])#创建指定维度的单位张量
filled_tsr = tf.fill([row_dim,col_dim],42)#创建指定维度的常数填充的张量

constant_tsr = tf.constant([1,2,3])#用已知常数张量创建一个张量
constant_tsr = tf.constant(42,[row_dim,col_dim])#.constant也可以广播一个值为数组，然后模拟tf。fill

# 2.相似形状的张量

#新建一个与给定的tensor类型大小一致的tensor，其所有元素为0或者1
zeros_similar = tf.zeros_like(constant_str)
ones_similiar = tf.ones_like(constant_str)  #需要给定张量，因此初始化需要按序进行，不可一次性初始化所有张量

# 3序列张量
# 可创建指定间隔的张量。下面函数输出与range（）函数和numpy的linespace（）函数输出类似
linear_tsr = tf.linspace(start = 0,stop=1,step=3)#返回的张量是[0.0, 0.5, 1.0]序列。
integer_seq_tsr = tf.range(start=6,limit=15,delta=3)#rang()函数使用方式如此，输出[6,9,12]，不包含limit值

# 4随机张量

# 4.1生成均匀分布的随机数 使用  td.random_uniform()函数
#随机分布为从minval（包含）开始到maxval（不包含）结束，即[ );
randunif_tsr = tf.random_uniform([row_dim,col_dim],minval=0,maxval=1)

# 4.2生成带有指定边界的正态分布的随机数，其正态分布的随机数位于指定均值（期望）到两个标准差之间的区间
runcnorm_tsr = tf.truncated_normal([row_dim,col_dim],mean=0.0,stddev=1.0)

#4.3 张量/数组的随机化。tf.random_shuffle() 和 tf.random_crop()
shuffled_output = tf.random_shuffle(input_tensor)
cropped_output = tf.random_crop(input_tensor)
#tf.random_crop可实现对张量指定大小的随机裁剪
# 在本书的后面部分，会对具有3通道颜色的图像（height，width，3）进行随机剪裁。为了固定剪裁结果的一个维度，需要在相应的维度上赋其最大值：
croped_image = tf.random_crop(my_image,[height/2,width/2,3])



#张量创建完毕后，可以通过tf.Variable()函数封装张量来作为变量，使用方式如下
my_var = tf.Variable(tf.zeros([row_dim,col_dim]))


# 扩展 不一定得用tf内建函数，也可以使用tf.convert_to_tensor()将任意numpy数组转换为python列表，或者将常量转换为一个张量。
# convert_to_tensor（）也可以接受张量作为输入