from socket import *
import time

for i in range(3):
    try:
        #send 3 UDP packets to the server
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.settimeout(5)
        sock.sendto(b'I am here', ('127.0.0.1', 1234))
        (data,address) = sock.recvfrom(1024)
        sock.close()
        print(address)
        print(data)
    except Exception as e:
        print("Error : Packet was lost : "+str(e))