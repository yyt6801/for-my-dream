import re

# 读取日志文件
with open(r'e:\OneDrive\Desktop\RollData-240812.log', 'r') as file:
    lines = file.readlines()

# 反向查找最后一个包含 "Stand 7" 的段落
stand_7_data = []
for line in reversed(lines):
    if "Stand 7" in line:
        stand_7_data.append(line.strip())
        if len(stand_7_data) == 4:  # 只需要最后的四项
            break

# 解析所需信息
results = []
for entry in reversed(stand_7_data):
    match = re.search(r'Stand 7\s+(WrTop|WrBot|BurTop|BurBot)\s+(\S+)\s+Dia\s+([\d.]+),\s+Qual=\s+(\S+),\s+Grindtyp=\s+(\S+)', entry)
    if match:
        results.append({
            'Type': match.group(1),
            'Roll Number': match.group(2),
            'Diameter': match.group(3),
            'Quality': match.group(4),
            'Grind Type': match.group(5)
        })

# 输出结果
for result in results:
    print(result)