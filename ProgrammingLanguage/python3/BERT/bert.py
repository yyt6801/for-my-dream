from transformers import BertTokenizer, BertModel
import torch
from transformers import logging
logging.set_verbosity_error()

# 初始化分词器和模型
# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
model = BertModel.from_pretrained('bert-base-uncased')

# 文章文本
text = '''高素质技术技能人才中的“高素质”“技术型”“技能型”和“技术技能型”几个要素，不仅要求明确人才培养的规格特征、规格要素和考评中的“双重”“双技”和“双向”维度，而且需要重塑高素质技术技能人才培养的全新理念，提高培养高素质技术技能人才的“双师”素质，全程性地创新高素质技术技能人才的培养模式，开发高素质技术技能人才培养的适用教材，构建教学相长、教赛相长、教研相长的高素质技术技能人才的教学方法，创新高素质技术技能人才的评价模式。'''

# 对文本进行编码
encoded_input = tokenizer(text, return_tensors='pt', max_length=512, truncation=True)
output = model(**encoded_input)

# 获取所有token的嵌入表示
embeddings = output.last_hidden_state.squeeze()

# 使用嵌入表示来提取关键词
# 这里需要一个额外的方法来从嵌入中提取关键词，比如使用聚类或者抽取嵌入向量中最重要的特征
# 这部分代码取决于你选择的关键词提取方法

# 示例：提取每个词的嵌入向量的norm，选择norm最大的词作为关键词
norms = torch.norm(embeddings, dim=1)
_, indices = torch.topk(norms, k=5)  # 提取前5个关键词
keywords = [tokenizer.decode([encoded_input['input_ids'][0][i]]) for i in indices]

print(keywords)