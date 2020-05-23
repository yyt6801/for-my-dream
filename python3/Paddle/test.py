# 加载库
import paddle.fluid as fluid
import numpy

# 定义输入数据
train_data = numpy.array([[1.0], [2.0], [3.0], [4.0]]).astype('float32')
y_true = numpy.array([[2.0], [4.0], [6.0], [8.0]]).astype('float32')

# 组建网络
x = fluid.data(name="x", shape=[None, 1], dtype='float32')
y = fluid.data(name="y", shape=[None, 1], dtype='float32')
y_predict = fluid.layers.fc(input=x, size=1, act=None)

# 定义损失函数
cost = fluid.layers.square_error_cost(input=y_predict, label=y)
avg_cost = fluid.layers.mean(cost)

# 选择优化方法
sgd_optimizer = fluid.optimizer.SGD(learning_rate=0.01)
sgd_optimizer.minimize(avg_cost)

# 网络参数初始化
cpu = fluid.CPUPlace()
exe = fluid.Executor(cpu)
exe.run(fluid.default_startup_program())

# 开始训练，迭代100次
for i in range(100):
    outs = exe.run(feed={
        'x': train_data,
        'y': y_true
    },
                   fetch_list=[y_predict, avg_cost])

# 输出训练结果
print(outs)
