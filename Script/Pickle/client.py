#!/bin/python
import pickle
import subprocess
import socket
import base64
import time
import random

hote = "localhost"
port = 5000


while True:
    s = socket.socket()
    s.connect((hote, port))
    lines = open('message.list').read().splitlines()
    theLine =random.choice(lines)

    s.send(b'===PACKED WITH PYTHON PICKLE FRAME===' + base64.b64encode(pickle.dumps(theLine)))
    s.close()
    time.sleep(10)
