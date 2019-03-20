from socket import *
import sys
import time
import datetime

sock = socket(AF_INET, SOCK_DGRAM)
#sock.settimeout(10)
try :
    sock.bind(('127.0.0.1',1234))
except Exception as e:
    print(str(e))

while True :
    (data,address) = sock.recvfrom(1024)
    print(str(datetime.datetime.now()))
    print(address)
    print(data)
    f = open('pingLogs.txt','a')
    f.write(str(datetime.datetime.now()) + " : " + str(address[0]) + " - " + str(data) + "\n")
    f.close()
    if data:
        sock.sendto(b'Ok', address)
    else :
        sock.close()
        sys.exit()
    
sock.close()