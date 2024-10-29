import time
import sys
import os
import stomp
# user = os.getenv("ACTIVEMQ_USER") or "admin"
user = "admin"
# password = os.getenv("ACTIVEMQ_PASSWORD") or "password"
password = "123456"
# host = os.getenv("ACTIVEMQ_HOST") or "localhost"
host = "localhost"
# port = os.getenv("ACTIVEMQ_PORT") or 61613
port = os.getenv("ACTIVEMQ_PORT") or 61616
# port = 61613
dest="test"
messages = 10000
data = "test from BeijingJiaotong"

conn = stomp.Connection(host_and_ports=[(host, port)])
# conn.start()
conn.connect(login=user, passcode=password)

for i in range(0, messages):
    conn.send(body=str(i), destination=dest, persistent='false')

# conn.send(body="SHUTDOWN", destination=dest, persistent='false')

conn.disconnect()
