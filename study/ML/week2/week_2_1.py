#Minimizing Cost
import tensorflow as tf
import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5, 6]
Y = [1, 2, 3, 4, 5, 6]

W = tf.placeholder(tf.float32)

# Our hypothesis for linear model X * W
hypo = X * W

# cost/loss function
cost = tf.reduce_mean(tf.square(hypo - Y))

# Launch the graph in a session.
sess = tf.Session()

# Variables for plotting cost function
W_his = []
cost_his = []

for i in range(-30, 50):
    curr_W = i * 0.1
    curr_cost = sess.run(cost, feed_dict={W: curr_W})
    W_his.append(curr_W)
    cost_his.append(curr_cost)

# Show the cost function
plt.plot(W_his, cost_his)
plt.show()
