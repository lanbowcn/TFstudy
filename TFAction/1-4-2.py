import tensorflow as tf

#返回一个op，表示给变量x加1的操作
x = tf.Variable(0.0)
x_plus_1 = tf.assign_add(x,1)

#control_dependencies的意义是，在执行with包含的内容（在这里就是 y = x）前
#先执行control_dependencies中的内容（在这里就是 x_plus_1）
with tf.control_dependencies([x_plus_1]):
    y=x
    z = tf.identity(x)
init = tf.global_variables_initializer()
with tf.Session() as session:
    init.run()
    for i in range(5):
        print(y.eval())#相当于sess.run(y)，由于control_dependencies的所以执行print前都会先执行x_plus_1
        print(z.eval())
