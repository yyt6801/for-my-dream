# 创建UDP服务器示例：
# 1、创建socket套接字
# 2、绑定
# 3、接受连接
# 4、发送数据
# 5、关闭

from socket import *
 
s= socket(AF_INET, SOCK_DGRAM) # 数据报式的套接字
s.bind(('127.0.0.1', 8080))
 
while True:
    data, address = s.recvfrom(1024)
    print data, address,type(data)
    s.sendto('this is the UDP server', address)

s.close()