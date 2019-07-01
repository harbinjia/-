#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 19-4-29 下午11:28 
# @Author : ho-ho
# @Site :  
# @File : tklearn1.py 
# @Description: 
# -------------------------------------------------------------------------------------


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
"""
class HelloApp:

    def __init__(self, root):
        self.label = Label(root, text="Who are you")
        self.label.grid(row=0, column=0)

        Button(root, text="Click Me", command=self.update).grid(row=1, column=0)

    def update(self):
        self.label.config(text='I am Alfred')


def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
"""
"""
不起作用
def printHello():
    print("hello")

root = Tk()

Button(root, text='click me', command=printHello).pack()
# Label(root, text="Hello, Tkinter!").pack()
"""
# root = Tk()
"""naw = ttk.Button(root, text="click me")
w.pack()
# 修改按钮文本值
# w['text'] = "Push me"
# w.config(text="push me")

def callback():
     messagebox.showinfo("what","are you")
w.config(command = callback)
"""
"""
ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()

f1 = ttk.Frame(root)
f1.pack()
f1.config(height = 100, width = 200)
f1.config(relief = RIDGE)
f2 = ttk.Frame(root)
f2.pack()
f2.config(height = 300, width = 400)
f2.config(relief = SUNKEN)

Button(f1, text = 'Click Me on Frame 1').pack()
Button(f2, text = 'Click Me on Frame 2').pack()
f1.config(padding = (300, 150))
"""
"""w = ttk.Notebook(root)
w.pack()

frame1 = ttk.Frame(w)
frame2 = ttk.Frame(w)
w.add(frame1, text = 'One')
w.add(frame2, text = 'Two')
ttk.Button(frame1, text = 'Click Me').pack()

frame3 = ttk.Frame(w)
w.insert(1, frame3, text = 'Three')
# notebook.forget(1)
# notebook.add(frame3, text = 'Three')

w.select(2)
print(w.index(w.select()))
# w.select(2)

w.tab(1, state = 'disabled')
# w.tab(1, state = 'hidden')
# w.tab(1, state = 'normal')
# w.tab(1, 'text')
# w.tab(1)"""
"""
# w = PanedWindow(orient=VERTICAL)
# w.pack(fill=BOTH, expand=1)

# top = Label(w, text="top pane")
# w.add(top)

# bottom = Label(w, text="bottom pane")
# w.add(bottom)


w = ttk.PanedWindow(orient = HORIZONTAL)
w.pack(fill = BOTH, expand = True)

f1 = ttk.Frame(w, width = 100, height = 300, relief = SUNKEN)
f2 = ttk.Frame(w, width = 400, height = 400, relief = SUNKEN)
w.add(f1, weight = 1)
w.add(f2, weight = 4)

f3 = ttk.Frame(w, width = 50, height = 50, relief = SUNKEN)
w.insert(1, f3)

top = Label(f1, text="top pane")
top.pack()

# bottom = Label(w, text="bottom pane")
# w.add(bottom)

# panedwindow.forget(1)
"""
"""
w = Toplevel(root)
w.title('New Window')

#w.lower()
w.lift(root)

# w.state('zoomed')
# w.state('withdrawn')
# w.state('iconic')
# w.state('normal')
# print(w.state())
# wi.state('normal')

# window.iconify()
# window.deiconify()

#w.geometry('640x480+50+100')
# print(window.geometry())
# window.resizable(False, False)
# window.maxsize(640, 480)
# window.minsize(200, 200)
# window.resizable(True, True)

# root.destroy()
"""
"""
Label(root, text = 'Green', background = 'Green').grid(row = 0, column = 0)
Label(root, text = 'Orange', background = 'Orange').grid(row = 0, column = 1)
Label(root, text = 'Yellow', background = 'yellow').grid(row = 0, column = 2, rowspan = 2)
Label(root, text = 'Blue', background = 'Blue').grid(row = 1, column = 0, columnspan = 2)

# root.rowconfigure(0, weight = 1)
# root.rowconfigure(1, weight = 3)
# root.columnconfigure(2, weight = 1)
"""
"""
Label(root, text = 'Hello, Tkinter!',
          background = 'yellow').pack(side = LEFT, anchor = 'nw')
Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(side = LEFT, padx = 10, pady = 10)
Label(root, text = 'Hello, Tkinter!',
          background = 'green').pack(side = LEFT, ipadx = 10, ipady = 10)
"""
"""
root.geometry('640x480+200+200')

Label(root, text = 'Yellow', background = 'yellow').place(x = 100, y = 5)
Label(root, text = 'Blue', background = 'blue').place(relx = 0.5, rely = 0.5,anchor='center')
Label(root, text = 'Green', background = 'green').place(relx = 0.5, x = 100, rely=0.5,y=50)
Label(root, text = 'Orange', background = 'orange').place(relx = 1.0, x = -5, y = 5,anchor='ne')
"""

"""
# 画布
c = Canvas(root)
c.pack()
c.config(width = 640, height = 480)

#line = c.create_line(160, 360, 480, 120, fill = 'blue', width = 5)
# c.itemconfigure(line, fill = 'green')
# print(c.coords(line))
# c.coords(line, 0, 0, 320, 240, 640, 0)

# c.itemconfigure(line, smooth = True)
# c.itemconfigure(line, splinesteps = 5)
# c.itemconfigure(line, splinesteps = 100)
# c.delete(line)

# rect = c.create_rectangle(160, 120, 480, 360)
# c.itemconfigure(rect, fill = 'yellow')
#oval = c.create_oval(160, 120, 480, 360)
# arc = c.create_arc(160, 1, 480, 240)
# c.itemconfigure(arc, start = 0, extent = 180, fill = 'green')
#poly = c.create_polygon(160, 360, 320, 480, 480, 360, fill = 'blue')
text = c.create_text(320, 240, text = '文本分类', font = ('Courier', 32, 'bold'))

# logo = PhotoImage(file = 'python_logo.gif') # Change path as needed
# image = c.create_image(320, 240, image = logo)

# c.lift(text)
# c.lower(image)
# c.lower(image, text)

button = Button(c, text = 'Click Me')
c.create_window(320, 60, window = button)

# canvas.itemconfigure(rect, tags = ('shape'))
# canvas.itemconfigure(oval, tags = ('shape', 'round'))
# canvas.itemconfigure('shape', fill = 'grey')
# print(canvas.gettags(oval))

"""
"""
更新标签内容
def update():
	label.config(text = 'Paris')

label = Label(root, text='Answer')
label.pack()

Button(root, text="Capital of France", command=update).pack()
"""
"""
def mouse_press(event):
    global prev
    prev = event

def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5)
    prev = event

root = Tk()

canvas = Canvas(root, width = 640, height = 480,
                background = 'white')
canvas.pack()
canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)"""

"""
label = Label(root, text = 'Label 1')
label.pack()

label.bind('<ButtonPress>', lambda e: print('Button Press'))
label.bind('<2>', lambda e: print('Mouse Press'))"""

"""
entry = Entry(root)
entry.pack()

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))
root.mainloop()
"""

"""
class HelloApp:

    def __init__(self, master):
        self.label = Label(master, text="Hello, Tkinter!")
        self.label.grid(row=0, column=0, columnspan=2)

        Button(master, text="Texas",
               command=self.texas_hello).grid(row=1, column=0)

        Button(master, text="Hawaii",
               command=self.hawaii_hello).grid(row=1, column=1)

    def texas_hello(self):
        self.label.config(text='Howdy, Tkinter!')

    def hawaii_hello(self):
        self.label.config(text='Aloha, Tkinter!')


def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()


if __name__ == "__main__": main()
"""

"""
class Feedback:

    def __init__(self, master):
        # master.title('Explore California Feedback')
        # master.resizable(False, False)
        # master.configure(background = '#e1d8b9')

        # self.style = Style()
        # self.style.configure('TFrame', background = '#e1d8b9')
        # self.style.configure('TButton', background = '#e1d8b9')
        # self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
        # self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        self.frame_header = Frame(master)
        self.frame_header.pack()

        self.logo = PhotoImage(file='mysql.png')
        Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)
        Label(self.frame_header, text='Thanks for Exploring!').grid(row=0, column=1)
        Label(self.frame_header, wraplength=300,
              text=("We're glad you chose Explore California for your recent adventure.  "
                    "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(row=1, column=1)

        self.frame_content = Frame(master)
        self.frame_content.pack()

        Label(self.frame_content, text='Name:').grid(row=0, column=0, padx=5, sticky='sw')
        Label(self.frame_content, text='Email:').grid(row=0, column=1, padx=5, sticky='sw')
        Label(self.frame_content, text='Comments:').grid(row=2, column=0, padx=5, sticky='sw')

        self.entry_name = Entry(self.frame_content, width=24, font=('Arial', 10))
        self.entry_email = Entry(self.frame_content, width=24, font=('Arial', 10))
        self.text_comments = Text(self.frame_content, width=50, height=10, font=('Arial', 10))

        self.entry_name.grid(row=1, column=0, padx=5)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)

        Button(self.frame_content, text='Submit',
               command=self.submit).grid(row=4, column=0, padx=5, pady=5, sticky='e')
        Button(self.frame_content, text='Clear',
               command=self.clear).grid(row=4, column=1, padx=5, pady=5, sticky='w')

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title='Explore California Feedback', message='Comments Submitted!')

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')


def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__ == "__main__": main()
"""


class Feedback:

    def __init__(self, master):
        master.title('Explore California Feedback')
        master.resizable(False, False)
        master.configure(background='#e1d8b9')

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('TLabel', background='#e1d8b9', font=('Arial', 11))
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))

        self.frame_header = Frame(master)
        self.frame_header.pack()

        self.logo = PhotoImage(file='mysql.png')
        Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)
        Label(self.frame_header, text='Thanks for Exploring!').grid(row=0, column=1)
        Label(self.frame_header, wraplength=300,
              text=("We're glad you chose Explore California for your recent adventure.  "
                    "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(row=1, column=1)

        self.frame_content = Frame(master)
        self.frame_content.pack()

        Label(self.frame_content, text='Name:').grid(row=0, column=0, padx=5, sticky='sw')
        Label(self.frame_content, text='Email:').grid(row=0, column=1, padx=5, sticky='sw')
        Label(self.frame_content, text='Comments:').grid(row=2, column=0, padx=5, sticky='sw')

        self.entry_name = Entry(self.frame_content, width=24)
        self.entry_email = Entry(self.frame_content, width=24)
        self.text_comments = Text(self.frame_content, width=50, height=10)

        self.entry_name.grid(row=1, column=0, padx=5)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)

        Button(self.frame_content, text='Submit', command=self.submit).grid(row=4, column=0, padx=5, pady=5, sticky='e')
        Button(self.frame_content, text='Clear', command=self.clear).grid(row=4, column=1, padx=5, pady=5, sticky='w')

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title='Feedback', message='Comments Submitted!')

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')


def main():
    root = Tk()
    app = Feedback(root)
    root.mainloop()


if __name__ == "__main__": main()

