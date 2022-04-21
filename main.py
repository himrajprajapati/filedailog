from tkinter import*
from tkinter.filedialog import *

root = Tk()
root.title('Open')
root.geometry('500x500+200+200')

def dialogbox() :
    dialog = askopenfile()
    mylabel= Label(text=dialog).pack()

btn = Button(text='open file', fg='blue', font=100, command=dialogbox).pack()

root.mainloop()