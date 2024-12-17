import re

def parse_log(file_path, target_pid):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 用于存储找到的最新数据段
    latest_data = []
    found_target = False

    # 反向遍历文件行以找到最新的 PID 数据
    for line in reversed(lines):
        if f'ProfPt: {target_pid}' in line:
            found_target = True
            continue
        
        if found_target:
            if line.startswith('PRE'):
                latest_data.append(line.strip())
                if len(latest_data) == 8:  # 包括字段名行和7行数据
                    break

    # 反转以恢复原始顺序
    latest_data.reverse()

    # 解析字段名行
    header_line = latest_data[0]
    headers = re.split(r'\s+', header_line.strip())  # 使用一个或多个空格分割字段名

    # 解析数据行
    data_rows = [re.split(r'\s+', line.strip()) for line in latest_data[1:]]

    # 将解析的结果存储在字典中
    parsed_results = []
    for row in data_rows:
        # 确保每行数据的长度与字段名一致
        if len(row) == len(headers):
            result = {headers[i]: row[i] for i in range(len(headers))}
            parsed_results.append(result)
        else:
            print(f"警告: 数据行与字段名长度不匹配: {row}")

    # 打印结果
    for entry in parsed_results:
        print("解析结果:", entry)
    
    # 访问第1行的 'Eprof' 字段
    first_row_eprof = parsed_results[0]['Eprof']
    print("第1行的 Eprof 字段:", first_row_eprof)

    # 访问第2行的 'Pa' 字段（假设有第二行数据）
    second_row_pa = parsed_results[1]['Pa']
    print("第2行的 Pa 字段:", second_row_pa)

# 使用示例
parse_log(r'c:\Users\Yuan\Desktop\PreRG-240812.log', 'X24814903300')