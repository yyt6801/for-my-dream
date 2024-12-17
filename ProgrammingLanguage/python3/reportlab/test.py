# import matplotlib
# print(matplotlib.get_cachedir())


def replace_last_word(s, replacement):  
    # 从右侧分割字符串，最多分割成2部分  
    parts = s.rsplit('_', 1)  
    if len(parts) == 2:  
        # 用替换的单词组合字符串  
        return f"{parts[0]}_{replacement}"  
    else:  
        # 如果没有下划线，直接返回原字符串  
        return s  


sample_range_name = replace_last_word("S5_THK_HEAD_AVG", "RANGE")
print(sample_range_name)