from socket import *
import sys
import time
import random
import base64

sentences = [b'Meet me at the coffe machine',b'Wow the last company party was so lit',b'Hey is it right you hooked up with the boss wife ?',b'Send you a mail with my new meme',b'Did you watch the game last night ?',b'Lets grab lunch',b'Thanks God its Friday',b'Hey check out the image I just got']

while True:
    #check the flag file to send packet or not
    frun = open('DoNotTouch.txt','r')
    run = frun.read()
    if run == '1':
        try:
            print("new sock -------")
            #create a socket
            sock = socket(AF_INET, SOCK_STREAM)
            sock.settimeout(60)
            sock.connect(('127.0.0.1', 1337))
            #receive message, read it then send a random one
            data = sock.recv(1024)
            if data:
                print(data)
                time.sleep(30)
                toSend = sentences[random.randint(0,7)]
                print(toSend)
                if toSend != b'Hey check out the image I just got':
                    sock.send(toSend)
                else:
                    #if the previous message is set to send the picture : 
                    sock.send(toSend)
                    time.sleep(3)
                    img = open('knuckles.png','rb')
                    imgData = base64.b64encode(img.read())
                    sock.sendall(imgData)
            else:
                #close the socket
                sock.close()
                break
            sock.close()
            time.sleep(30)

        except Exception as e:
            print(str(e))
    #close the flag file
    frun.close()