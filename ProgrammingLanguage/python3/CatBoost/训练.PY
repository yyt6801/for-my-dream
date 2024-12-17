from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import pandas as pd

# 读取文件
excel_file = pd.ExcelFile('1.xlsx')

# 获取所有表名
sheet_names = excel_file.sheet_names
sheet_names

# 获取指定工作表中的数据
df = excel_file.parse('Sheet1')

# 查看数据的基本信息和前几行
print('数据基本信息：')
df.info()

# 查看数据集行数和列数
rows, columns = df.shape

if rows < 100 and columns < 20:
    # 短表数据（行数少于100且列数少于20）查看全量数据信息
    print('数据全部内容信息：')
    print(df.to_markdown(numalign='left', stralign='left'))
else:
    # 长表数据查看数据前几行信息
    print('数据前几行内容信息：')
    # print(df.head().to_markdown(numalign='left', stralign='left'))


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import catboost as cb

# 获取基本信息和特征数据（前 21 列）
X = df.iloc[:, :17]

# 获取判定结果（最后 1 列）
y = df.iloc[:, -1]

# 将判定结果转换为数值型标签
y = y.replace({'未跑偏': 0, '跑偏卷': 1})

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建 CatBoost 分类器
clf = cb.CatBoostClassifier(verbose=False)

# 使用训练集进行训练
clf.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = clf.predict(X_test)

# 计算评估指标
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# 输出评估指标
print('Accuracy:', accuracy)
print('Precision:', precision)
print('Recall:', recall)
print('F1-Score:', f1)

# 保存训练好的模型
clf.save_model('model.cbm')

