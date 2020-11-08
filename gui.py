from tkinter import *

def store_values():
    global day
    global sleep
    global wake
    global naps
    global steps
    global mood
    day = E1.get()
    sleep = E2.get()
    wake = E3.get()
    naps = E4.get()
    steps = E5.get()
    mood = E6.get()

    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    E4.delete(0, END)
    E5.delete(0, END)
    E6.delete(0, END)

    print(day, sleep, wake, naps, steps, mood)


top = Tk()
L1 = Label(top, text = "Please input today's date (eg. 1-Aug-20): ")
L1.place(x = 10,y = 10)
E1 = Entry(top, bd = 3)
E1.place(x = 240,y = 10)
L2 = Label(top,text = "At what time did you exactly sleep? ")
L2.place(x = 10,y = 50)
E2 = Entry(top,bd = 3)
E2.place(x = 220,y = 50)
L3 = Label(top,text = "What time did you wake up? ")
L3.place(x = 10,y = 90)
E3 = Entry(top,bd = 3)
E3.place(x = 200,y = 90)
L4 = Label(top, text = "Did you take a nap? If so, how long? ")
L4.place(x = 10, y = 130)
E4 = Entry(top, bd = 3)
E4.place(x = 220, y = 130)
L5 = Label(top, text = "How many steps did you take today? ")
L5.place(x = 10, y = 170)
E5 = Entry(top, bd = 3)
E5.place(x = 220, y = 170)
L6 = Label(top, text = "How was your mood? ")
L6.place(x = 10, y = 210)
E6 = Entry(top, bd = 3)
E6.place(x = 150, y = 210)
B = Button(top, text = "Submit", command = store_values)
B.place(x = 100, y = 290)
top.geometry("700x500+10+10")
top.mainloop()
