import tensorflow as tf

sess =tf.Session()
first_var = tf.Variable(tf.zeros([2,3]))

sess.run(first_var.initializer)
second_var = tf.Variable(tf.zeros_like(first_var))
#需要first_var的输出

sess.run(second_var.initializer)