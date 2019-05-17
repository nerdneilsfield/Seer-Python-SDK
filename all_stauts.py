from seer_sdk.connector import Connector
from seer_sdk.apis import *
import time
import logging

logging.basicConfig(filename='myapp.log', level=logging.WARNING)

conn = Connector('10.20.204.144', 19204)
conn.connect()

for i in STATUS: 
     data = conn.send(i)[1] 
     if data != None: data.print_data() 
     time.sleep(0.25)

conn.close()