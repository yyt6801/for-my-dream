import re

def parse_log_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 反向查找最新的包含 X24814903300 的段落
    for i in range(len(lines) - 1, -1, -1):
        if 'X24814903300' in lines[i]:
            # 找到 ID 行
            id_line = lines[i - 1].strip()
            data_line = lines[i].strip()
            # 找到 P 开头的行
            p_index = i + 2
            while p_index < len(lines) and not lines[p_index].startswith('P'):
                p_index += 1
            
            # 提取 MATNO
            matno_match = re.search(r'MATNO\s+(\d+)', id_line)
            matno = matno_match.group(1) if matno_match else None
            
            # 提取 CRT 和 WEAR
            crt_weary_data = []
            for j in range(p_index + 1, p_index + 8):  # 1~7行
                if j < len(lines):
                    crt_weary_values = lines[j].strip().split()
                    crt_weary_data.append((crt_weary_values[0], crt_weary_values[1]))  # CRT 和 WEAR
            
            return matno, crt_weary_data

# 使用示例
file_path = r'e:\OneDrive\Desktop\EngLog-240812.log'
matno, crt_weary_data = parse_log_file(file_path)

print(f'MATNO: {matno}')
print('CRT 和 WEAR 数据:')
for crt, wear in crt_weary_data:
    print(f'CRT: {crt}, WEAR: {wear}')