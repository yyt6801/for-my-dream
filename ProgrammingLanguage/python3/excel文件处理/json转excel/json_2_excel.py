import pandas as pd
import json

# 读取JSON文件
with open('test.json', 'r') as file:
    data = json.load(file)

# 提取curve数组
curve_data = data['data']['kv']
print(curve_data)

# 将数据转换为DataFrame
df = pd.DataFrame(curve_data)

# 将DataFrame写入Excel文件
df.to_excel('curve_data.xlsx', index=False)

print("数据已成功写入Excel文件")
