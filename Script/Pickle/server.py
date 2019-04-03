#!/bin/python
import socket
import pickle
import base64

host = "127.0.0.1"
port = 5000

mySocket = socket.socket()
mySocket.bind((host,port))
while True:
	frun = open('DoNotTouch.txt','r')
	run = frun.read()
		if run == '1':
		mySocket.listen(1)
		conn, addr = mySocket.accept()

		data = conn.recv(1024).decode()
		try:
			d = data.split("===PACKED WITH PYTHON PICKLE FRAME===")[1]
		except:
			pass
		decoded = base64.b64decode(d)
		pi = pickle.loads(decoded)
		print(pi)
