# 创建UDP客户端示例：
# 1、创建套接字
# 2、连接
# 3、发送数据
# 4、接收数据
# 5、关闭

from socket import *
 
HOST = '127.0.0.1';PORT = 8080;
addr = (HOST,PORT) # 设置IP、端口号、
s = socket(AF_INET, SOCK_DGRAM) # 建立UDP的socket 这个称之为套接字。
data = 'hello';
data = data.encode(encoding="utf-8") # 指定一个字符串，并转换成socket发送的二进制流。
while True:
    s.sendto(data, addr) # 发送数据
    # data, addr = s.recvfrom(1024) # 接收数据和返回地址
    print (data.decode(encoding="utf-8"))
    print(addr)
s.close()