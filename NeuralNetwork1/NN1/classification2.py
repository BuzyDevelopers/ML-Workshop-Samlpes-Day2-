import tensorflow as tf
import numpy
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import numpy as np 

X , Y = make_classification(2000, n_features = 10, n_informative = 8, n_clusters_per_class = 2)

Y = np.array([Y, -(Y-1)]).T 

X, X_test, Y, Y_test = train_test_split(X, Y)

total_batch = 100
#print(X, Y)

config = {
    "layer_1_ip" : 10,
    "layer_1_hidden" : 10,
    "layer_2_hidden" : 10,
    "layer_3_op" : 2
}

x_input  = tf.placeholder("float", [None, config['layer_1_ip']])
y_output = tf.placeholder("float", [None, config['layer_3_op']])

w = {
    'w1': tf.Variable(tf.random_normal([config['layer_1_ip'], config['layer_1_hidden']])),
    'w2': tf.Variable(tf.random_normal([config['layer_1_hidden'],  config['layer_2_hidden']])),
    'w3': tf.Variable(tf.random_normal([ config['layer_2_hidden'],  config['layer_3_op']]))
}

b = {
    'b1': tf.Variable(tf.random_normal(config["layer_1_hidden"])),
    'b2': tf.Variable(tf.random_normal(config["layer_2_hidden"])),
    'b3': tf.Variable(tf.random_normal(config["layer_3_op"]))
}

def multilayerPerceptron(x, w, b):

    l1 = tf.add(tf.matmul(x, w['w1']), b['b1'])
    l1 = tf.nn.relu(l1)
    l2 = tf.add(tf.matmul(l1, w['w2']), b['b2'])
    l2 = tf.nn.relu(l2)

    op = tf.add(tf.matmul(l2, w['w3']), b['b3'])

    return op

predictions = multilayerPerceptron(X, w, b)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predictions, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)

# Initializing the variables
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    # Training cycle
    for epoch in range(100):
        avg_cost = 0.
        total_batch = int(len(X)/batch_size)
        X_batches = np.array_split(X, total_batch)
        Y_batches = np.array_split(Y, total_batch)
        # Loop over all batches
        for i in range(total_batch):
            batch_x, batch_y = X_batches[i], Y_batches[i]
            # Run optimization op (backprop) and cost op (to get loss value)
            _, c = sess.run([optimizer, cost], feed_dict={x: batch_x,
                                                          y: batch_y})
            # Compute average loss
            avg_cost += c / total_batch
        # Display logs per epoch step
        if epoch % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))
    print("Optimization Finished!")

    # Test model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print("Accuracy:", accuracy.eval({x: X_test, y: Y_test}))
    global result 
    result = tf.argmax(pred, 1).eval({x: X_test, y: Y_test})