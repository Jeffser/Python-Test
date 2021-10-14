from tkinter import *
num=0
win = Tk()
win.geometry("360x800")
win.resizable(False, False)
win.title("Test Android")
lbl = Label(text="a", font="Arial, 24")
lbl.grid(row=0, column=0, columnspan=2)

def plus():
    global num
    num = num+1
    lbl.config(text=num)
def minus():
    global num
    num = num-1
    lbl.config(text=num)

btn = Button(text="+1", font = "Arial, 24", command=plus)
btn.grid(row=1, column=0)
btn2 = Button(text="-1", font = "Arial, 24", command=minus)
btn2.grid(row=1, column=1)
win.mainloop()
