#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 19-4-29 上午8:34 
# @Author : ho-ho
# @Site :  
# @File : gui.py 
# @Description: 
# -------------------------------------------------------------------------------------


from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
"""
top = Tk()   # 创建窗口对象的背景色

# 创建两个列表
li = ['C','Python','php','html','java']
movie = ['css','jquery','bootstrap']
# 创建两个列表组件
listb = Listbox(top)
listb2 = Listbox(top)
#插入数据
for item in li:
    listb.insert(0, item)

for item in movie:
    listb2.insert(0, item)
# 将小部件放置到主窗口
listb.pack()
listb2.pack()


def helloCallBack():
    messagebox.showinfo("hello python","hello ho")

B = Button(top, text="sub", conmmand=helloCallBack())
B.pack()
top.mainloop()   # 进入消息循环
"""
"""
top=Tk()
top.wm_title("菜单")
top.geometry("400x300+300+100")

# 创建一个菜单项，类似于导航栏
menubar=Menu(top)

# 创建菜单项
fmenu1=Menu(top)
for item in ['新建','打开','保存','另存为']:
    # 如果该菜单时顶层菜单的一个菜单项，则它添加的是下拉菜单的菜单项。
    fmenu1.add_command(label=item)

fmenu2=Menu(top)
for item in ['复制','粘贴','剪切']:
    fmenu2.add_command(label=item)

fmenu3=Menu(top)
for item in ['默认视图','新式视图']:
    fmenu3.add_command(label=item)

fmenu4=Menu(top)
for item in ["版权信息","其他说明"]:
    fmenu4.add_command(label=item)

# add_cascade 的一个很重要的属性就是 menu 属性，它指明了要把那个菜单级联到该菜单项上，
# 当然，还必不可少的就是 label 属性，用于指定该菜单项的名称
menubar.add_cascade(label="文件",menu=fmenu1)
menubar.add_cascade(label="编辑",menu=fmenu2)
menubar.add_cascade(label="视图",menu=fmenu3)
menubar.add_cascade(label="关于",menu=fmenu4)

# 最后可以用窗口的 menu 属性指定我们使用哪一个作为它的顶层菜单
top['menu']=menubar
top.mainloop()
"""

class Application(Frame):
    def __init__(self, master=None):  # master即是窗口管理器，用于管理窗口部件，如按钮标签等，顶级窗口master是None，即自己管理自己
        Frame.__init__(self, master)
        self.pack(expand=YES, fill=BOTH)  # 将widget加入到父容器中并实现布局
        self.window_init()
        self.createWidgets()

    def window_init(self):
        self.master.title('mooc平台师生互动类问题的文本分类')
        self.master.geometry("500x400")

    def createWidgets(self):
        # 创建主窗口，用于容纳其他组件
        # self.root = Tk()
        # 给主窗口设置标题内容
        # self.root.title("文本自动分类")
        # 设置窗口大小
        # self.root.geometry('300x200')
        # 设置窗口宽不可变，高可变
        # self.root.resizable(width=False, height=True)

        # self.frm = Frame(self.root)
        # left
        # self.frm_L = Frame(self.frm)
        # Label(self.frm_L, text="请选择一个文本:", font=("Arial",14))
        # 创建一个按钮选择文件
        # self.choose = Button(self.frm_L, command=self.find_file(), text="选择文件")

        # left
        self.fm = Frame(self)
        self.fm_left = Frame(self.fm)
        self.fm_right = Frame(self.fm)
        self.fm_left_top = Frame(self.fm_left)
        self.fm_left_bottom = Frame(self.fm_left)

        self.text = Label(self.fm_left_top, text="输入测试文本:")
        self.text.pack(side=LEFT)
        #self.chooseButton = Button(self.fm_left_top, command=self.find_file, text="选择文件")
        #self.chooseButton.pack(side=LEFT, padx=20)
        self.input=Entry(self.fm_left_top, width=20)
        self.input.pack(side=LEFT, padx=20)
        self.fm_left_top.pack(side=TOP, fill='x')

        v = IntVar()  # 获取单选按钮value参数对应的值
        self.ran1 = Radiobutton(self.fm_left_bottom, text="文本类别", variable=v, value=1)
        self.ran1.pack(side=LEFT)
        self.ran2 = Radiobutton(self.fm_left_bottom, text="文本关键词", variable=v, value=2)
        self.ran2.pack(side=LEFT, fill='y', padx=20)
        self.fm_left_bottom.pack(side=TOP, pady=20, fill='x')

        self.left_select = Frame(self.fm_left)
        self.select_button = Button(self.left_select, command=self.select, text="查询")
        self.select_button.pack(side=LEFT)
        self.left_select.pack(side=TOP, pady=10, fill='x')
        self.fm_left.pack(side=LEFT, padx=50, pady=30, fill='x')

        self.show_info = Listbox(self.fm_right)
        self.show_info.pack(expand=YES, fill=BOTH)
        self.fm_right.pack(side=RIGHT,expand=YES,fill=BOTH,padx=10)
        self.fm.pack(side=TOP, expand=YES, fill='x')

    def find_file(self):
        a = tkinter.filedialog.askopenfilename()
        print(a)

    def select(self):
        pass


if __name__ == '__main__':
    app = Application()
    app.mainloop()
