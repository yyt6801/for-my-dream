
# -*-coding:utf-8-*-
import sys
import time
import stomp
user = "admin"
password = "123456"
host = "localhost"
port = 61616
dest="test"

destination = sys.argv[1:2] or ["/topic/event"]
print(sys.argv)
destination = destination[0]
class MyListener(object):
    def __init__(self, conn):
        self.conn = conn
        self.count = 0
        self.start = time.time()
    def on_error(self, headers, message):
        print('received an error %s' % message)
    def on_message(self, headers, message):
        print(message)
        if message == "SHUTDOWN":
            conn.disconnect()
            sys.exit(0)
        else:
            print(message)

conn = stomp.Connection(host_and_ports=[(host, port)])
conn.set_listener('', MyListener(conn))
# conn.start()
conn.connect(login=user, passcode=password)
conn.subscribe(destination=dest, ack='auto', id="")
print("Waiting for messages...")
while 1:
    time.sleep(10)
