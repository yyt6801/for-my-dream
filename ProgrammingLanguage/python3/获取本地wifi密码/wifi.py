import subprocess
 
# 获取wifi列表
output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True).stdout.decode('gbk').split('\n')
wifis = [line.split(':')[1][1:-1] for line in output if "所有用户配置文件" in line]
 
# 查看每个wifi对应的密码
for wifi in wifis:
    results = subprocess.run(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear'],
                             capture_output=True).stdout.decode('gbk', errors='ignore').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "关键内容" in line]
    try:
        print(f'wifi名：{wifi}，密码:{results[0]}')
    except IndexError:
        print(f'wifi名：{wifi}，密码:无法提取')
input('按enter确认并退出')