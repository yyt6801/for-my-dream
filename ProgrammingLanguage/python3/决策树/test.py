from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# 假设我们有一些历史输入数据X和对应的输出结果Y
# 例如，X可以是二维数组，其中每一行代表一个输入实例，每一列代表一个特征
# Y是一个数组，包含每个输入实例对应的输出结果
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
Y = np.array([0, 1, 0, 1, 0])

# 将数据集分为训练集和测试集
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 创建决策树分类器实例
classifier = DecisionTreeClassifier()

# 使用训练集数据训练模型
classifier.fit(X_train, Y_train)

# 使用测试集数据评估模型
predictions = classifier.predict(X_test)
print("预测结果:", predictions)
print("实际结果:", Y_test)
print("准确率:", accuracy_score(Y_test, predictions))

# 现在，你可以使用这个训练好的模型来对新的输入数据进行预测
# 例如：
new_input = np.array([[2, 3]])
new_output = classifier.predict(new_input)
print("新输入的预测输出:", new_output)