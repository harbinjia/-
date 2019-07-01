#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 19-4-30 上午9:17 
# @Author : ho-ho
# @Site :  
# @File : gpu.py 
# @Description: 
# -------------------------------------------------------------------------------------


from tkinter import *
from tkinter import messagebox
import PyQt5

class feedback:

    def __init__(self, master):
        master.title('classification')
        master.geometry('400x300+0+0')
        master.resizable(False, False)

        self.frame_header = Frame(master)
        self.frame_header.pack()

        Label(self.frame_header, text='文本分析-hoho',font=('Arial',14)).grid(row=0, column=1,padx=5,pady=15)

        self.frame_content = Frame(master)
        self.frame_content.pack()

        Label(self.frame_content, text='输入测试语句:').grid(row=1, column=0, padx=5, sticky='e')
        self.entry_text = Entry(self.frame_content, width=30)
        self.entry_text.grid(row=1, column=1,columnspan=2)

        """
        var = StringVar()
        self.ran1 = Radiobutton(self.frame_content, text='类别', variable=var, value=1)
        self.ran1.grid(row=2, column=0, padx=5, pady=5)
        self.ran2 = Radiobutton(self.frame_content, text='关键词', variable=var, value=2)
        self.ran2.grid(row=2, column=1, padx=10, pady=5)
        """

        Button(self.frame_content, text='查询', command=self.submit).grid(row=2, column=1, padx=5, pady=10)
        Button(self.frame_content, text='清空', command=self.clear).grid(row=2, column=2, padx=5, pady=10)

        self.frame_result = Frame(master)
        self.frame_result.pack()

        Label(self.frame_result, text='结果显示:').grid(row=3, column=0,sticky=E)
        self.show_res = Listbox(self.frame_result, width=40).grid(row=4, column=1, pady=5,columnspan=2)

    def submit(self):
        print('TEXT: {}'.format(self.entry_text.get()))
        self.clear()
        messagebox.showinfo(title='Feedback', message='Comments Submitted!')
        self.text=self.entry_text.get()


    def clear(self):
        self.entry_text.delete(0, 'end')





def main():
    root = Tk()
    app = feedback(root)
    root.mainloop()


if __name__ == "__main__":
    main()
