# -*-coding:utf-8-*-
import sys
import time
import stomp
user = "admin"
password = "admin"
host = "170.0.200.11"
port = 61616

# 定义一个监听类，里面有一个 on_message 方法
class SampleListener(object):
    def on_message(self, headers, message):
        print(message)
        
# 连接消息队列
def connect():
    # reconnect_attempts_max 设置成 -1 ， 连接不成功，一直尝试重连
    conn = stomp.Connection([('170.0.200.11', 61616)],reconnect_attempts_max=-1)
    conn.set_listener('listener_name', SampleListener())
    conn.connect()
    conn.subscribe('C621_exception',123)
    return conn

if __name__ == '__main__':
   # 连接消息队列
   conn = connect()
   while True:
       # 每 5秒判断一次，是否断开连接（因为没有找到断连得回调，只好自己定时判断）
       time.sleep(5)
       if not conn.is_connected():
           # 断连重连
           conn = connect()
   conn.disconnect()
