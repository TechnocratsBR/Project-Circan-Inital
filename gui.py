from tkinter import *

def store_values():
    global E1
    global E2
    global E3
    global E4
    global E5
    a = E1.get()
    b = E2.get()
    c = E3.get()
    d = E4.get()
    e = E5.get()


top = Tk()
L1 = Label(top, text = "a")
L1.place(x = 10,y = 10)
E1 = Entry(top, bd = 3)
E1.place(x = 60,y = 10)
L2 = Label(top,text = "b")
L2.place(x = 10,y = 50)
E2 = Entry(top,bd = 3)
E2.place(x = 60,y = 50)
L3 = Label(top,text = "c")
L3.place(x = 10,y = 90)
E3 = Entry(top,bd = 3)
E3.place(x = 60,y = 90)
L4 = Label(top, text = "d")
L4.place(x = 10, y = 130)
E4 = Entry(top, bd = 3)
E4.place(x = 60, y = 130)
L5 = Label(top, text = "e")
L5.place(x = 10, y = 170)
E5 = Entry(top, bd = 3)
E5.place(x = 60, y = 170)
B = Button(top, text = "Submit", command = store_values)
B.place(x = 100, y = 210)
top.geometry("250x500+10+10")
top.mainloop()
