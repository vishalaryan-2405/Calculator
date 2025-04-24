from tkinter import *

window = Tk()
window.geometry('700x700')

entry = Entry(window, width=50, borderwidth=5)
entry.place(x=0, y=0)

def click(num):
    result = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(result) + str(num))

# Number Buttons
Button(window, text='1', width=10, command=lambda: click(1)).place(x=10, y=60)
Button(window, text='2', width=10, command=lambda: click(2)).place(x=100, y=60)
Button(window, text='3', width=10, command=lambda: click(3)).place(x=190, y=60)
Button(window, text='4', width=10, command=lambda: click(4)).place(x=10, y=100)
Button(window, text='5', width=10, command=lambda: click(5)).place(x=100, y=100)
Button(window, text='6', width=10, command=lambda: click(6)).place(x=190, y=100)
Button(window, text='7', width=10, command=lambda: click(7)).place(x=10, y=140)
Button(window, text='8', width=10, command=lambda: click(8)).place(x=100, y=140)
Button(window, text='9', width=10, command=lambda: click(9)).place(x=190, y=140)
Button(window, text='0', width=10, command=lambda: click(0)).place(x=10, y=180)

# Operations
def add():
    global math, i
    i = int(entry.get())
    math = 'addition'
    entry.delete(0, END)

def sub():
    global math, i
    i = int(entry.get())
    math = 'subtraction'
    entry.delete(0, END)

def multi():
    global math, i
    i = int(entry.get())
    math = 'multiplication'
    entry.delete(0, END)

def div():
    global math, i
    i = int(entry.get())
    math = 'division'
    entry.delete(0, END)

Button(window, text='+', width=10, command=add).place(x=100, y=180)
Button(window, text='-', width=10, command=sub).place(x=190, y=180)
Button(window, text='*', width=10, command=multi).place(x=10, y=220)
Button(window, text='/', width=10, command=div).place(x=100, y=220)

def equal():
    n2 = entry.get()
    entry.delete(0, END)
    try:
        if math == 'addition':
            entry.insert(0, i + int(n2))
        elif math == 'subtraction':
            entry.insert(0, i - int(n2))
        elif math == 'multiplication':
            entry.insert(0, i * int(n2))
        elif math == 'division':
            if int(n2) == 0:
                entry.insert(0, "Error: Div by 0")
            else:
                entry.insert(0, i / int(n2))
    except Exception as e:
        entry.insert(0, "Error")

Button(window, text='=', width=10, command=equal).place(x=190, y=220)

def clear():
    entry.delete(0, END)

Button(window, text='clear', width=10, command=clear).place(x=10, y=260)

window.mainloop()
