import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x400')
# 一定要在window后面
var = tk.StringVar()  # 文字变量存储器
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


def print_selection():
    l.config(text='you have selected ' + var.get())


r1 = tk.Radiobutton(window, text='A', variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='B', variable=var, value='B', command=print_selection)
r2.pack()
window.mainloop()
