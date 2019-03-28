from socket import *
import sys
import time
import random

sentences = ["Meet me at the coffe machine","Wow the last company party was so lit","Hey is it right you hooked up with the boss wife ?","Send you a mail with my new meme","Did you watch the game last night ?","Lets grab lunch","Thanks God its Friday"]

#set up the server socket
sock = socket(AF_INET, SOCK_STREAM)
sock.settimeout(60)
try :
    sock.bind(('127.0.0.1',1337))
except Exception as e:
    print(str(e))

sock.listen(3)

#keep running, but do nothing if the flag file is at 0
while True:
    frun = open('DoNotTouch.txt','r')
    run = frun.read()
    if run == '1':
        try: 
            print("---")
            #wait a new connection
            connexion, address = sock.accept()
            print("connected from {}".format(address))
            #open socket as a file
            f = connexion.makefile('rw', buffering=None)
            toSend = sentences[random.randint(0,6)]
            print(toSend)
            #send his random message then wait the answer
            f.write(toSend)
            f.flush()
            data = f.readline()
            #close the socket
            f.close()
            connexion.close()
        except Exception as e:
            pass
        
    frun.close()
    
sock.close()