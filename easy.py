#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 19-4-29 下午8:06 
# @Author : ho-ho
# @Site :  
# @File : easy.py 
# @Description: 
# -------------------------------------------------------------------------------------


import tkinter


class FindLocation(object):
    def __init__(self):
        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("文本分类")

        # 创建一个输入框,并设置尺寸
        self.ip_input = tkinter.Entry(self.root, width=30)

        # 创建一个回显列表
        self.display_info = tkinter.Listbox(self.root, width=50)

        # 创建一个查询结果的按钮
        self.result_button = tkinter.Button(self.root, command=self.find_position, text="查询")

        # 清空按钮
        self.clear_button = tkinter.Button(self.root, command=self.clear, text="清空")

    # 完成布局
    def gui_arrang(self):
        self.ip_input.pack()
        self.display_info.pack()
        self.result_button.pack(side='left',padx=100,fill='x')
        self.clear_button.pack(side='right',padx=100,fill='x')

    # 根据ip查找地理位置
    def find_position(self):
        # 获取输入信息
        self.ip_addr = self.ip_input.get()
        aim = self.gi.record_by_name(self.ip_addr)
        # 为了避免非法值,导致程序崩溃,有兴趣可以用正则写一下具体的规则,我为了便于新手理解,减少代码量,就直接粗放的过滤了
        try:

            # 获取目标城市
            city = aim["city"]
            # 获取目标国家
            country = aim["country_name"]
            # 获取目标地区
            region_code = aim["region_code"]
            # 获取目标经度
            longitude = aim["longitude"]
            # 获取目标纬度
            latitude = aim["latitude"]
        except:
            pass

        # 创建临时列表
        the_ip_info = ["关键词:" + str(latitude), "类别:" + str(longitude),"准确度:" + str(city)]
        # 清空回显列表可见部分,类似clear命令
        #for item in range(10):
        #    self.display_info.insert(0, "")

        # 为回显列表赋值
        for item in the_ip_info:
            self.display_info.insert(0, item)
        # 这里的返回值,没啥用,就是为了好看
        return the_ip_info

    def clear(self):
        self.display_info.delete(0, 'end')


def main():
    # 初始化对象
    FL = FindLocation()
    # 进行布局
    FL.gui_arrang()
    # 主程序执行
    tkinter.mainloop()
    pass


if __name__ == "__main__":
    main()