import tkinter as tkinter
from tkinter import messagebox 

root = tkinter.Tk()
root.title('App')
root.geometry('300x400')

Window1 = tkinter.LabelFrame(root, text="Entry details")
Window1.grid(row=2,column=1,padx=10,pady=2)

Window2 = tkinter.LabelFrame(root,text="List Details")
Window2.grid(row=3, column=1,padx=10,pady=2)

#function to store input from entry and show message box on click of button
def Message():
    name = input.get()
    if name != '' :
        messagebox.showinfo('message',f'Hi {name}, you have been added to the list') #shows message box
        lb.insert(tkinter.END,name)#inserts the variable of name in the list at end
    else:
        messagebox.showinfo('message',"Enter your name!")

def ClearListBox():
    lb.delete(0,tkinter.END)
    messagebox.showinfo('message','List has been cleared')

Heading = tkinter.Label(root, text='My App')
Heading.grid(row=1,columnspan=3)

one = tkinter.Label(Window1, text='Enter your Name')
one.grid(row=2,column = 1,padx=5)

#Entry box  to retrieve users input
input = tkinter.Entry(Window1)
input.grid(row=2, column=2,padx=5)

#button to initiate function to show message box
EntBtn = tkinter.Button(Window1, text='Enter', command=Message) 
EntBtn.grid(row=3, column = 2,pady=10)

#List to show items in the list
lb = tkinter.Listbox(Window2)
lb.grid(row=4, column=1,padx=10,pady=5)

#Clear ListBox Button 
ClrBtn = tkinter.Button(Window2, text='Clear', command=ClearListBox)
ClrBtn.grid(row=5 ,column=1,padx=10)

root.mainloop()