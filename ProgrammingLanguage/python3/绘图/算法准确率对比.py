import matplotlib.pyplot as plt

# 测试集编号
test_sets = [1, 2, 3, 4, 5]

# 各算法准确率
accuracy_a = [0.899, 0.88, 0.805, 0.82, 0.86]
accuracy_b = [0.802, 0.73, 0.86, 0.79, 0.82]
accuracy_c = [0.823, 0.81, 0.84, 0.75, 0.70]

# 设置柱状图宽度
bar_width = 0.2
index = range(len(test_sets))

# 绘制算法A的柱状图
plt.bar([i for i in index], accuracy_a, width=bar_width, label='BP神经网络')
# 绘制算法B的柱状图（位置偏移一个宽度）
plt.bar([i + bar_width for i in index], accuracy_b, width=bar_width, label='CatBoost')
# 绘制算法C的柱状图（位置再偏移一个宽度）
plt.bar([i + 2 * bar_width for i in index], accuracy_c, width=bar_width, label='XGBoost')

# 设置坐标轴标签等
plt.xlabel('测试集编号')
plt.ylabel('准确率')
plt.title('不同算法预测精度对比')
plt.xticks([i + bar_width for i in index], test_sets)
plt.legend()
plt.show()