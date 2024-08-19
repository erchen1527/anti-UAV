from scapy.all import *
import time


def ip():
    IP = '192.168.43.' + str(random.randint(2, 254))
    return IP


def port():
    Port = random.randint(2000, 20000)
    return Port

# 心跳包
data1 = b'\xfe\x09\x0f\xff\xbe\x00\x00\x00\x00\x00\x06\x08\x00\x00\x03\xcc\xdd'

# 请求连接
data2 = b"\xfe\x06\xff\xff\xbe\x42\x02\x00\x01\x01\x01\x01\x1b\xa0"

# while True:
#     ip_src = ip()
#     port_src = port()
#
#     send(IP(src=ip_src, dst='192.168.43.123')/UDP(sport=port_src, dport=14555)/data)

while True:
    send(IP(src='192.168.43.149', dst='192.168.43.148') / UDP(sport=14556, dport=14550) / data1)
    # send(IP(src='192.168.43.148', dst='192.168.43.123') / UDP(sport=14550, dport=14555) / data2)

    time.sleep(1)

    # break