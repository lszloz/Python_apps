# 广播接收
"""
1.创建UDP套接字
2.设置套接字为可以接收广播
3.选择一个接收的端口
"""
from socket import *
# 创建UDP套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 设置套接字为可以接收广播
sockfd.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

#
sockfd.bind(('0.0.0.0', 7890))  # 空字符串''等价于'0.0.0.0'

while True:
    try:
        msg, addr = sockfd.recvfrom(1024)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
    else:
        print(msg.decode())

sockfd.close()
