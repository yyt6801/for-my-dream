import re

def parse_log_file(file_path, target_id):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # 反向查找最后一个包含目标卷号的行
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].startswith("ID") and target_id in lines[i]:
            # 提取MATNO
            matno = lines[i + 1].split()[7]  # MATNO在第8列（索引7）
            break
    else:
        return None  # 如果没有找到卷号，返回None

    # 查找以P开头的行
    for j in range(i + 3, len(lines)):
        if lines[j].startswith("P"):
            # 提取CRT和WEAR字段名
            field_names = lines[j].split()
            crt_index = field_names.index("CRT")
            wear_index = field_names.index("WEAR")
            break
    else:
        return None  # 如果没有找到P行，返回None

    # 提取机架数据
    crt_values = []
    wear_values = []
    for k in range(j + 1, j + 8):  # 机架数据在P行下方的7行
        if k < len(lines) and lines[k].strip():
            values = lines[k].split()
            crt_values.append(values[crt_index])
            wear_values.append(values[wear_index])

    return {
        "MATNO": matno,
        "CRT": crt_values,
        "WEAR": wear_values
    }

# 使用示例
file_path = r'e:\OneDrive\Desktop\EngLog-240812.log'  # 日志文件路径
target_id = "X24814903300"
result = parse_log_file(file_path, target_id)

if result:
    print("MATNO:", result["MATNO"])
    print("CRT:", result["CRT"])
    print("WEAR:", result["WEAR"])
else:
    print("未找到指定卷号的数据。")