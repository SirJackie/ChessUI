import ctypes
from tkinter import *
from tkinter.ttk import *


def fac(x):
    if x==0 or x==1:
        return 1
    elif x>1:
        return x*fac(x-1)


root=Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)
root.title('计算阶乘')
frame1=Frame(root)
frame1.pack(side='top',anchor='center',expand='yes')
lable1=Label(frame1,text='input')
lable2=Label(frame1,text='output')
entry1=Entry(frame1)
entry2=Entry(frame1)


def button1_clicked():
    entry2.delete(0,END)
    entry2.insert(0,str(fac(eval(entry1.get()))))


button1=Button(frame1,text='Run',command=button1_clicked)
button2=Button(frame1,text='Quit',command=root.quit)
lable1.grid(row=0,column=0,pady=3,padx=3)
lable2.grid(row=1,column=0,pady=3,padx=3)
entry1.grid(row=0,column=1,pady=3,padx=3)
entry2.grid(row=1,column=1,pady=3,padx=3)
button1.grid(row=2,column=0,sticky=W,pady=3,padx=3)
button2.grid(row=2,column=1,sticky=E,pady=3,padx=3)

root.mainloop()
