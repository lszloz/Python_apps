"""
udp套接字客户端
"""

from socket import *

# 服务器地址
HOST = '127.0.0.1'
PORT = 8880
ADDR = (HOST,PORT)

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#　收发消息
while True:
    data = input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print("From server:",msg.decode())

sockfd.close()







