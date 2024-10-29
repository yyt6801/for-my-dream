import paddle
import paddle.nn.functional as F
import numpy as np
from paddle.vision.transforms import Compose, Resize, Transpose, Normalize

#准备数据
t = Compose([Resize(size=96),Normalize(mean=[127.5, 127.5, 127.5], std=[127.5, 127.5, 127.5], data_format='HWC'),Transpose()]) #数据转换
cifar10_train = paddle.vision.datasets.cifar.Cifar10(mode='train', transform=t, backend='cv2')
cifar10_test = paddle.vision.datasets.cifar.Cifar10(mode="test", transform=t, backend='cv2')

#构建模型
class Residual(paddle.nn.Layer):
    def __init__(self, in_channel, out_channel, use_conv1x1=False, stride=1):
        super(Residual, self).__init__()
        self.conv1 = paddle.nn.Conv2D(in_channel, out_channel, kernel_size=3, padding=1, stride=stride)
        self.conv2 = paddle.nn.Conv2D(out_channel, out_channel, kernel_size=3, padding=1)
        if use_conv1x1: #使用1x1卷积核
            self.conv3 = paddle.nn.Conv2D(in_channel, out_channel, kernel_size=1, stride=stride)
        else:
            self.conv3 = None
        self.batchNorm1 = paddle.nn.BatchNorm2D(out_channel)
        self.batchNorm2 = paddle.nn.BatchNorm2D(out_channel)

    def forward(self, x):
        y = F.relu(self.batchNorm1(self.conv1(x)))
        y = self.batchNorm2(self.conv2(y))
        if self.conv3:
            x = self.conv3(x)
        out = F.relu(y+x) #核心代码
        return out

def ResNetBlock(in_channel, out_channel, num_layers, is_first=False):
    if is_first:
        assert in_channel == out_channel
    block_list = []
    for i in range(num_layers):
        if i == 0 and not is_first:
            block_list.append(Residual(in_channel, out_channel, use_conv1x1=True, stride=2))
        else:
            block_list.append(Residual(out_channel, out_channel))
    resNetBlock = paddle.nn.Sequential(*block_list) #用*号可以把list列表展开为元素
    return resNetBlock

class ResNetModel(paddle.nn.Layer):
    def __init__(self):
        super(ResNetModel, self).__init__()
        self.b1 = paddle.nn.Sequential(
                    paddle.nn.Conv2D(3, 64, kernel_size=7, stride=2, padding=3),
                    paddle.nn.BatchNorm2D(64), 
                    paddle.nn.ReLU(),
                    paddle.nn.MaxPool2D(kernel_size=3, stride=2, padding=1))
        self.b2 = ResNetBlock(64, 64, 2, is_first=True)
        self.b3 = ResNetBlock(64, 128, 2)
        self.b4 = ResNetBlock(128, 256, 2)
        self.b5 = ResNetBlock(256, 512, 2)
        self.AvgPool = paddle.nn.AvgPool2D(2)
        self.flatten = paddle.nn.Flatten()
        self.Linear = paddle.nn.Linear(512, 10)
        
    def forward(self, x):
        x = self.b1(x)
        x = self.b2(x)
        x = self.b3(x)
        x = self.b4(x)
        x = self.b5(x)
        x = self.AvgPool(x)
        x = self.flatten(x)
        x = self.Linear(x)
        return x

epoch_num = 100
batch_size = 512
learning_rate = 0.001

val_acc_history = []
val_loss_history = []

def train(model):
    #开启训练模式
    model.train()
    #优化器
    opt = paddle.optimizer.Adam(learning_rate=learning_rate, parameters=model.parameters())
    #数据小批量加载器
    train_loader = paddle.io.DataLoader(cifar10_train, shuffle=True, batch_size=batch_size)
    valid_loader = paddle.io.DataLoader(cifar10_test, batch_size=batch_size)

    for epoch in range(epoch_num):
        for batch_id, data in enumerate(train_loader()):
            x_data = paddle.cast(data[0], 'float32')
            y_data = paddle.cast(data[1], 'int64')
            y_data = paddle.reshape(y_data, (-1, 1))
            y_predict = model(x_data)
            loss = F.cross_entropy(y_predict, y_data)
            loss.backward()
            opt.step()
            opt.clear_grad()
        print("训练轮次: {}; 损失: {}".format(epoch, loss.numpy()))

        #启动评估模式
        model.eval()
        accuracies = []
        losses = []
        for batch_id, data in enumerate(valid_loader()):
            x_data = paddle.cast(data[0], 'float32')
            y_data = paddle.cast(data[1], 'int64')
            y_data = paddle.reshape(y_data, (-1, 1))
            y_predict = model(x_data)
            loss = F.cross_entropy(y_predict, y_data)
            acc = paddle.metric.accuracy(y_predict, y_data)
            accuracies.append(np.mean(acc.numpy()))
            losses.append(np.mean(loss.numpy()))

        avg_acc, avg_loss = np.mean(accuracies), np.mean(losses)
        print("评估准确度为：{}；损失为：{}".format(avg_acc, avg_loss))
        val_acc_history.append(avg_acc)
        val_loss_history.append(avg_loss)
        model.train()

model = ResNetModel()
train(model)