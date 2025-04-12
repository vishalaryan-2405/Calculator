from tkinter import *
window=Tk()
window.geometry('700x700')

entry=Entry(window,width=50,borderwidth=5)
entry.place(x=0,y=0)
def click(num):
    result=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(result)+str(num))


button=Button(window,text='1',width=10,command= lambda:click(1))
button.place(x=10,y=60)
button1=Button(window,text='2',width=10,command=lambda:click(2))
button1.place(x=100, y=60)
button2=Button(window,text='3',width=10,command=lambda:click(3))
button2.place(x=190,y=60)
button3=Button(window,text='4',width=10,command=lambda:click(4))
button3.place(x=10,y=100)
button4=Button(window,text='5',width=10,command=lambda:click(5))
button4.place(x=100,y=100)
button5=Button(window,text='6',width=10,command=lambda:click(6))
button5.place(x=190,y=100)
button6=Button(window,text='7',width=10,command=lambda:click(7))
button6.place(x=10,y=140)
button7=Button(window,text='8',width=10,command=lambda:click(8))
button7.place(x=100,y=140)
button8=Button(window,text='9',width=10,command=lambda:click(9))
button8.place(x=190,y=140)
button9=Button(window,text='0',width=10,command=lambda:click(0))
button9.place(x=10,y=180)
def add():
    n1=entry.get()
    global math
    math='addition'
    global i
    i=int(n1)
    entry.delete(0,END)

button10=Button(window,text='+',width=10,command=add)
button10.place(x=100,y=180)
def sub():
    n1=entry.get()
    global math
    math='subtraction'
    global i
    i=int(n1)
    entry.delete(0,END)
button11=Button(window,text='-',width=10,command=sub)
button11.place(x=190,y=180)
def multi():
    n1=entry.get()
    global math
    math='multipication'
    global i
    i=int(n1)
    entry.delete(0,END)

button2=Button(window,text='*',width=10,command=multi)
button2.place(x=10,y=220)
def div():
    n1=entry.get()
    global math
    math='division'
    global i
    i=int(n1)
    entry.delete(0,END)
button2=Button(window,text='/',width=10,command=div)
button2.place(x=100,y=220)
def equal():
    n2=entry.get()
    entry.delete(0,END)
    if math=='addition':
        entry.insert(0,i+int(n2))
    elif math=='subtraction':
        entry.insert(0,i-int(n2))
    elif math=='multipication':
        entry.insert(0,i*int(n2))
    else:
        entry.insert(0,i/int(n2))
button2=Button(window,text='=',width=10,comma=equal)
button2.place(x=190,y=220)
def clear():
    entry.delete(0,END)
button2=Button(window,text='clear',width=10,command=clear)
button2.place(x=10,y=260)

mainloop()