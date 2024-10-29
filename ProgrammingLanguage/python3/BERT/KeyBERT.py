from keybert import KeyBERT

doc = "这是你想要提取关键词的文本"
model = KeyBERT('distilbert-base-nli-mean-tokens')
keywords = model.extract_keywords(doc)

print(keywords)