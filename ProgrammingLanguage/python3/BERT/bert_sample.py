# 使用transformers库来运行BERT模型
# 这段代码将加载预训练的BERT模型和分词器，对一些文本进行编码，并通过BERT模型获取输出。
# 请确保在运行这些命令之前，你的Miniconda环境是激活的。如果你希望在GPU上运行BERT模型，你还需要确保你的机器上安装了正确版本的CUDA。

# from transformers import BertTokenizer, BertModel

# # 加载分词器和BERT模型
# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# model = BertModel.from_pretrained('bert-base-uncased')

# # 编码文本
# input_text = "Here is some text to encode"
# encoded_input = tokenizer(input_text, return_tensors='pt')

# # 获取BERT模型的输出
# output = model(**encoded_input)

# print(output)



# 1. 加载BERT模型：首先，你需要加载预训练的BERT模型。你可以使用Hugging Face的transformers库来实现这一点。
# 2. 词嵌入：然后，你可以使用BERT模型将文章的每个词转换为向量。这些向量捕获了词的语义信息。
# 3. 关键词提取：最后，你可以使用这些词嵌入来提取关键词。一种方法是使用聚类算法（如K-means）将词嵌入分组，然后选择每个组中最接近中心的词作为关键词。

from transformers import BertModel, BertTokenizer
import torch

# 加载预训练的BERT模型和分词器
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# 对文章进行分词
inputs = tokenizer("Your article text here", return_tensors="pt")

# 获取词嵌入
outputs = model(**inputs)
# print(output)
embeddings = outputs.last_hidden_state
print(embeddings)

# 现在你可以使用这些嵌入来提取关键词
# 例如，你可以使用聚类算法将词嵌入分组，然后选择每个组中最接近中心的词作为关键词