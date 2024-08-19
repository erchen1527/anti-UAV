import socket
import random

def ip():
    IP = '192.168.43.' + str(random.randint(2, 254))
    return IP

def port():
    Port = random.randint(2000, 20000)
    return Port

data = b'\xfe\x09\x0f\xff\xbe\x00\x00\x00\x00\x00\x06\x08\x00\x00\x03\xcc\xdd'

# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 设置源IP地址和源端口号
s.bind((ip(), port()))

# 设置目的IP地址和目的端口号
dst_ip = '192.168.43.148'
dst_port = 14550

# 发送数据
s.sendto(data, (dst_ip, dst_port))
