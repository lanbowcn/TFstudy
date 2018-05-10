import  tensorflow as tf
import numpy as np

# 矩阵操作

sess = tf.Session()
identity_matrix = tf.diag([1.0, 1.0, 1.0])
A = tf.truncated_normal([2, 3])
B = tf.fill([2, 3], 5.0)
C = tf.random_uniform([3, 2])
D = tf.convert_to_tensor(np.array([[1., 2., 3.], [-3., -7., -1.], [0., 5., -2.]]))
print(sess.run(identity_matrix))
print(sess.run(A))
print(sess.run(B))
print(sess.run(C))
print(sess.run(D))

print(sess.run(A+B))
print(sess.run(B-B))

# 矩阵乘法函数matmul（）可以通过参数指定在矩阵乘法操作前是否进行矩阵转置。
print(sess.run(tf.matmul(B, identity_matrix)))

#矩阵转置
print(sess.run(tf.transpose(C)))

# 计算行列式的值
print(sess.run(tf.matrix_determinant(D)))

#矩阵求逆
#矩阵需要为对称正定矩阵或者可进行LU分解
print(sess.run(tf.matrix_inverse(D)))#此处求逆方法为Cholesky矩阵分解法（又称平方根法）

# 矩阵分解
# 此处使用Cholesky分解法
print(sess.run(tf.cholesky(identity_matrix)))

#求特征值和特征向量（矩阵的特征分解）
print(sess.run(tf.self_adjoint_eig))#输出第一行为特征值，剩下的向量是对应的向量