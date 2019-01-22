import tensorflow as tf

x = [1,2,3,4,5,6]
y = [1,2,3,4,5,6]

w = tf.Variable(tf.random_normal([1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

hypo = w*x+b

cost = tf.reduce_mean(tf.square(hypo-y))

train = tf.train.GradientDescentOptimizer(learning_rate = 0.01).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for i in range(1 ,2001):
    sess.run(train)
    if (i%100):
        print (step, sess.run(cost), sess.run(w), sess.run(b))
