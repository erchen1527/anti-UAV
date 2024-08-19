# -*- coding: utf-8 -*-
# time : 2022/12/11 21:51
# file : test.py
# author : erchen
# description :


# from scapy.all import *
# import time
#
# # 解锁/原id
# data1 = bytes.fromhex('fe21c8ffbe4c0000803f00000000000000000000000000000000000000000000000090010101009045')
#
# # 锁定/原id
# data2 = bytes.fromhex('fe2140ffbe4c000000000000000000000000000000000000000000000000000000009001010100c486')
#
# # 解锁/非原id
# data3 = bytes.fromhex('fe216afbfb4c0000803f00000000000000000000000000000000000000000000000090010101003684')
#
# # 锁定/非原id
# data4 = bytes.fromhex('fe2140fbfb4c0000000000000000000000000000000000000000000000000000000090010101008133')
#
# while True:
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data3)
#     #
#     time.sleep(4)
#
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data4)
#     break




# from scapy.all import *
# import time
#
# '''
# fe065effbe420200010102017f6a
# fe0660ffbe420200010106010cd3
# fe0662ffbe42040001010a014085
# fe0664ffbe42040001010b01eb2a
# fe0667ffbe42020001010c019000
# fe0668ffbe42020001010101a3e3
# fe066affbe4202000101030139fd
# '''
#
# data1 = bytes.fromhex('fe065effbe420200010102017f6a')
# data2 = bytes.fromhex('fe0660ffbe420200010106010cd3')
# data3 = bytes.fromhex('fe0662ffbe42040001010a014085')
# data4 = bytes.fromhex('fe0664ffbe42040001010b01eb2a')
# data5 = bytes.fromhex('fe0667ffbe42020001010c019000')
# data6 = bytes.fromhex('fe0668ffbe42020001010101a3e3')
# data7 = bytes.fromhex('fe066affbe4202000101030139fd')
# data8 = bytes.fromhex('fe0246ffbe150101b2 a8')
#
# while True:
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data1)
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data2)
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data3)
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data4)
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data5)
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data6)
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data7)
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data8)
#     # time.sleep(0.1)
#
#     # break


# from scapy.all import *
# import time
#
# data2 = b'\xfe\x21\x40\xff\xbe\x4c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x01\x01\x00\xc4\x86'
#
# while True:
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data2)
#     # break

# from scapy.all import *
# import time
#
# data6 = b'\xfe\x21\x7f\xff\xbe\x4c\x00\x00\x80\x3f\x00\x00\x10\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb0\x00\x01\x01\x00\x87\xb2'
#
# data7 = b'\xfe\x06\x80\xff\xbe\x0b\x09\x00\x00\x00\x01\x01\xfb\x57'
#
# data8 = b'\xfe\x06\x81\xff\xbe\x0b\x09\x00\x00\x00\x01\x01\x6a\x02'
#
# while True:
#     # Guided模
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data6)
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data7)
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data8)
#
#     # break

# from scapy.all import *
# import time
#
# # Guided模式
# data1 = b'\xfe\x21\x16\xff\xbe\x4c\x00\x00\x80\x3f\x00\x00\x80\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb0\x00\x01\x01\x00\xc4\x84'
#
# data2 = b'\xfe\x06\xc8\xff\xbe\x0b\x04\x00\x00\x00\x01\x01\x1b\x08'
#
# data3 = b'\xfe\x06\xc9\xff\xbe\x0b\x04\x00\x00\x00\x01\x01\x8a\x5d'
#
# # 解锁
# data4 = b'\xfe\x21\x6a\xff\xbe\x4c\x00\x00\x80\x3f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x01\x01\x01\x00\x73\x31'
#
# # 起飞
# data5 = b'\xfe\x21\x16\xff\xbe\x4c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x48\x42\x16\x00\x01\x01\x00\x1a\xda'
#
# while True:
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data1)
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data2)
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data3)
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data4)
#     send(IP(src='192.168.1.148', dst='192.168.1.123') / UDP(sport=14550, dport=14555) / data5)
#
#     # break

# btn_heart = tk.Button(self.initface, text='心跳包', command=self.crc_check)
# btn_heart.pack()
# btn_unlock = tk.Button(self.initface, text='解锁', command=self.crc_check)
# btn_unlock.pack()
# btn_lock = tk.Button(self.initface, text='锁定', command=self.crc_check)
# btn_lock.pack()
# btn_takeoff = tk.Button(self.initface, text='起飞', command=self.crc_check)
# btn_takeoff.pack()
# btn_custom = tk.Button(self.initface, text='自定义', command=self.crc_check)
# btn_custom.pack()
# btn_back = tk.Button(self.initface, text='返回', command=self.crc_check)
# btn_back.pack()

# from scapy.all import *
# from scapy.layers.inet import IP, UDP
#
# data = bytes.fromhex('fe21e5ffbe4c0000803f00000000000000000000000000000000000000000000000090010101000ada')
# send(IP(src='192.168.43.148', dst='192.168.43.123') / UDP(sport=14550, dport=14555) / data)

from tkinter import *
# import tkMessageBox
import tkinter

top = Tk()
top.geometry('1000x600')
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
C1 = Checkbutton(top, text="a")
C2 = Checkbutton(top, text="b")
C3 = Checkbutton(top, text="c")
C4 = Checkbutton(top, text="d")
C1.pack(side='left')
C2.pack(side='left')
C3.pack(side='left')
C4.pack(side='left')
# txt = Text(top)
# txt.pack()
top.mainloop()


