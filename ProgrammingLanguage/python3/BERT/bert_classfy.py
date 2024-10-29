from transformers import pipeline

# 文章文本
text = '''Haha, today is a nice day!'''

nlp = pipeline("feature-extraction")
vector = nlp(text)
print(vector)