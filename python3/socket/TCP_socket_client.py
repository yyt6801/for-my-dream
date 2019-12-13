# 创建TCP客户端示例：
# 1、创建socket对象
# 2、连接主机,应当是一个元组
# 3、发送数据
# 4、接收数据
# 5、关闭

import socket
 
p = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
p.connect(('127.0.0.1',8080))
while 1:
    msg = input('please input')
    # 防止输入空消息
    if not msg:
        continue
    p.send(msg.encode('utf-8')) # 收发消息一定要二进制，记得编码
    if msg == '1':
        break
p.close()