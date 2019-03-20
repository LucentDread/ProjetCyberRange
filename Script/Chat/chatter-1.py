from socket import *
import sys
import time
import random

sentences = ["Meet me at the coffe machine","Wow the last company party was so lit","Hey is it right you hooked up with the boss wife ?","Send you a mail with my new meme","Did you watch the game last night ?","Lets grab lunch","Thanks God its Friday"]

sock = socket(AF_INET, SOCK_STREAM)
sock.settimeout(60)
try :
    sock.bind(('127.0.0.1',1337))
except Exception as e:
    print(str(e))

sock.listen(3)

while True:
    try: 
        print("---")
        connexion, address = sock.accept()
        print("connected from {}".format(address))
        f = connexion.makefile('rw', buffering=None)
        toSend = sentences[random.randint(0,6)]
        print(toSend)
        f.write(toSend)
        f.flush()
        data = f.readline()
        if data:
            print(data)
        else:
            f.close()
            connexion.close()
        f.close()
        connexion.close()
    except Exception as e:
        pass
    
sock.close()