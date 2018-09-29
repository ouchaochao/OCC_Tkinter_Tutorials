import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x400')
# 一定要在window后面
var = tk.StringVar()  # 文字变量存储器

on_hit = False


def hit_me():
    global on_hit
    if not on_hit:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')


l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15, height=2)
l.pack()  # 固定窗口位置

b = tk.Button(window, text='hit', width=15, height=2, command=hit_me)
b.pack()

# 这里是窗口的内容
window.mainloop()
