"""
UDP套接字服务端
"""
from socket import *

# 创建数据包套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
sockfd.bind(('127.0.0.1', 8880))

# 收发消息
while True:
    try:
        data, addr = sockfd.recvfrom(512)
        print("Connected from:", addr)
    except KeyboardInterrupt:
        print("退出服务")
        break
    print("收到的消息:",data.decode())
    n = sockfd.sendto(b'Copy that.', addr)  # 回复消息

# 关闭套接字
sockfd.close()
