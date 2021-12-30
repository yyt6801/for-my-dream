import socket
import sys
import getFileContent
#声明一个将要绑定的IP和端口，这里是用本地地址
server_address = ('localhost', 8080)
class WebServer():
    def run(self):
        print(sys.stderr, 'starting up on %s port %s' % server_address) 
        #实例化一个Socket
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #绑定IP和端口
        sock.bind(server_address)
        #设置监听
        sock.listen(1)
        #这里首先给个死循环，其实这里是需要多线程的，再后续版本将会实现
        while True:
            #接受客户端的请求并得到请求信息和请求的端口信息
            connection, client_address = sock.accept()
            print >>sys.stderr, 'waiting for a connection'
            try:
                #获取请求信息
                data = connection.recv(1024)
                if data:
                    #发送请求信息
                    connection.sendall(getFileContent.getHtmlFile(data))
            finally:
                connection.close()

if __name__ == '__main__':
    server=WebServer()
    server.run()