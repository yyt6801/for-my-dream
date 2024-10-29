# -*-coding:utf-8-*-
import stomp
import time

user = "admin"
password = "123456"
host = "170.0.200.11"
port = 61616

queue_name = '/queue/SampleQueue'
topic_name = 'C621_exception'
listener_name = 'failover'

class SampleListener(object):
    def on_message(self, headers, message):
        print(headers)
        print(message)

# 推送到队列queue
def send_to_queue(msg):
    conn = stomp.Connection([(host,port)])
    conn.connect()
    conn.send(queue_name, msg)
    conn.disconnect()

#推送到主题
def send_to_topic(msg):
    conn = stomp.Connection([(host,port)])
    conn.connect()
    conn.send(topic_name, msg)
    conn.disconnect()

##从队列接收消息
def receive_from_queue():
    conn = stomp.Connection([(host,port)])
    conn.set_listener(listener_name, SampleListener())
    conn.connect()
    conn.subscribe(queue_name)
    time.sleep(1) # secs
    conn.disconnect()

##从主题接收消息
def receive_from_topic():
    conn = stomp.Connection([(host,port)])
    conn.set_listener(listener_name, SampleListener())
    conn.connect()
    # conn.subscribe(topic_name)
    conn.subscribe(topic_name, ack='auto', id="")
    while 1:
        # send_to_topic('test')
        time.sleep(3) # secs

    conn.disconnect()

if __name__=='__main__':
    # send_to_queue('len 123')
    # receive_from_queue()
    receive_from_topic()