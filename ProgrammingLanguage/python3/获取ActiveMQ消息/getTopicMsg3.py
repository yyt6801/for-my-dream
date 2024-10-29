# -*-coding:utf-8-*-
import stomp
import time

__listener_name = 'SampleListener'
__topic_name1 = 'C621_exception'
__host = '170.0.200.11'
__port = 61616

class SampleListener(object):
    def on_message(self, headers, message):
        print('每5秒发送一次')
        print('headers: %s' % headers['destination'])
        print('message: %s\n' % message)


## 从主题接收消息
def receive_from_topic():

    conn = stomp.Connection10([(__host, __port)])
    conn.set_listener(__listener_name, SampleListener())
    conn.connect()
    conn.subscribe(__topic_name1)
    while True:
        pass
    conn.disconnect()


if __name__ == '__main__':

    receive_from_topic()
