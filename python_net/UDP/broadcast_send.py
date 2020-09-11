# 广播发送
from socket import *
from time import sleep

# 选定一个广播地址
dest = ('127.0.0.1', 7890)

# 创建数据报套接字
s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_BROADCAST, 0)

data = "小喇叭开始广播啦"

mark = 0
while True:
    sleep(2)
    s.sendto(data.encode(), dest)
    mark += 1
    if mark > 10:
        break

s.close()
