# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# # 更新并丰富的数据
# data = {
#     "工匠精神": 0.546,
#     "领军人才": 0.136,
#     "创新团队": 0.131,
#     "信息化": 0.021,
#     "多元融合型人才": 0.076,
#     "实践性知识": 0.023,
#     "素质": 0.020,
#     "大师": 0.009,
#     "复合型人才": 0.002,
#     "技术创新": 0.045,
#     "团队合作": 0.060,
#     "领导力": 0.035,
#     "市场洞察": 0.025,
#     "客户关系": 0.018,
#     "项目管理": 0.040,
#     "持续学习": 0.030,
#     "解决方案专家": 0.022,
#     "国际视野": 0.015,
#     "创业精神": 0.027,
#     "社会责任": 0.013
# }

# # 生成词云
# wordcloud = WordCloud(font_path='simhei.ttf', width=800, height=400, background_color='white').generate_from_frequencies(data)

# # 显示词云
# plt.figure(figsize=(10, 5))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 数据：关键词及其权重（这里假设每个词的权重相同，设为1）
data = {
"终身学习":0.411,
"能力":0.235,
"贯通培养":0.167,
"职业适应性":0.098,
"职业素养":0.034,
"职业技能提升":0.021,
"高技能人才必备能力":0.006,
"人才":0.012,
"素质":0.01,
"大师工作室":0.01,
}

# 生成词云
wordcloud = WordCloud(font_path='simhei.ttf', width=300, height=150, background_color='white').generate_from_frequencies(data)

# 显示词云
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()