# coding=utf8
import networkx as nx
import matplotlib.pyplot as plt

# 数据
data = {
    "教育学": 465, "哲学": 418, "经济学": 365, "劳动经济学": 296, "政治学": 270, "自动化": 227,
    "企业经济": 150, "宏观经济管理与可持续发展": 107, "工程科技": 75, "思想政治教育": 60,
    "中国政治与国际政治": 48, "社会科学": 42, "行政管理": 34, "经济体制改革": 32, "农业经济": 26,
    "电力工业": 25, "交通运输经济": 18, "石油天然气工业": 17, "冶金工业": 16, "金属学及金属工艺": 14
}

# 创建图
G = nx.Graph()

# 添加节点和边
for subject, weight in data.items():
    G.add_node(subject, size=weight)
    for other_subject in data:
        if other_subject != subject:
            # 这里简化处理，假设所有学科之间都有连接
            # 实际应用中应该基于学科间的实际共现关系来添加边
            G.add_edge(subject, other_subject, weight=min(data[subject], data[other_subject]))

# 绘制图
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, k=0.15, iterations=20)
sizes = [G.nodes[node]['size'] * 10 for node in G]  # 调整节点大小
nx.draw(G, pos, with_labels=True, node_size=sizes, font_size=8, edge_color="gray", linewidths=0.5, font_weight="bold")

plt.title("学科共现网络图")
plt.show()