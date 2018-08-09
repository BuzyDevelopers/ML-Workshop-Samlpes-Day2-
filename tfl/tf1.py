import tensorflow

x = tensorflow.constant([[1, 2, 3], [1, 2, 3], [1, 2, 3]], name = 'x')

w = tensorflow.constant([[1, 2, 3], [1, 2, 3], [1, 2, 3]], name = 'y')

c = tensorflow.matmul(x, w)

b = tensorflow.constant([[1, 2, 3], [1, 2, 3], [1, 2, 3]], name  = 'b')

result = tensorflow.add(c, b)

with tensorflow.Session() as sess:
    op = sess.run(result)
    tensorflow.summary.FileWriter('.', sess.graph)
    print(op)