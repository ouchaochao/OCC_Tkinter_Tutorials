import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x400')
# 一定要在window后面
var1 = tk.StringVar()  # 文字变量存储器
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
l.pack()


def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)


b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()
var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
lb = tk.Listbox(window, listvariable=var2)
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)
# lb.insert(1, 'first')
# lb.insert(2, 'second')
# lb.delete(2)
lb.pack()
window.mainloop()
