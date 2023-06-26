# 须将json文件和py程序放在同路径下，先cd至该路径再执行
import json
with open('fundCompany.json') as f:
    data = json.load(f)
print(type(data))  # Output: dict
print(data)