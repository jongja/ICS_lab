import tensorflow as tf

#definition X and Y data
x_data = [1, 2, 3, 4, 5, 6]
y_data = [1, 2, 3, 4, 5, 6]

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#y_data = x_data * W + b

hypothesis = x_data * W + b

cost = tf.reduce_mean(tf.square(hypothesis - y_data))

#minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(cost), sess.run(W), sess.run(b))