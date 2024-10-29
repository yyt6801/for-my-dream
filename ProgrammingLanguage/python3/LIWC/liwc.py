def liwc(text, dictionary):
    # 分割文本为单词
    words = text.lower().split()

    # 初始化计数器
    counts = {category: 0 for category in dictionary.keys()}

    # 计数
    for word in words:
        for category, category_words in dictionary.items():
            if word in category_words:
                counts[category] += 1

    # 计算频率
    total_words = len(words)
    frequencies = {category: count / total_words for category, count in counts.items()}

    return frequencies