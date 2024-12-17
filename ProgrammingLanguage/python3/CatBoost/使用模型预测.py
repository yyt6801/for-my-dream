import pandas as pd
import catboost as cb

# 使用训练好的CatBoost模型对新数据进行预测
clf = cb.CatBoostClassifier()
clf.load_model('model.cbm')  # 加载训练好的模型

# # 读取新的数据文件
# new_data = pd.read_excel('测试数据.xlsx')
# print(new_data)
# # 获取新的数据特征（前21列）
# X_new = new_data.iloc[:, :17]
# print(X_new)

# 构造数据
data = {
    '宽度': [1.252],
    '厚度': [0.5],
    '一次项系数最大值': [2.6499364],
    '一次项系数均值': [-0.565720101],
    '一次项系数超限次数': [34],
    '一次项系数绝对积分值': [2730.83859],
    '一次项系数归一后积分值': [2807.899178],
    '末机架速度最大值': [1302],
    '末机架速度均值': [1050.736993],
    '辊缝差最大值': [0.014],
    '辊缝差均值': [-0.086616641],
    '辊缝差最小值': [-0.112],
    '工作辊弯辊力最大值': [114],
    '工作辊弯辊力均值': [66.61720983],
    '中间辊弯辊力最大值': [371],
    '中间辊弯辊力均值': [367.0068611],
    '弯辊力差': [300.3896512]
        }

# 构造 DataFrame
X_new = pd.DataFrame(data)

y_pred_new = clf.predict(X_new)

# 输出预测结果
print('预测结果：')
print(y_pred_new)
