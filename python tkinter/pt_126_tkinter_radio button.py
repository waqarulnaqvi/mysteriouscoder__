# 19 6
from tkinter import *
from PIL import Image,ImageTk
#Almost everything in tkinter is a 2 step process except image in tkinter.

root=Tk()
root.geometry("500x400")
root.title("Radio button in tkinter")
root.iconbitmap('jarvis.ico')
img=ImageTk.PhotoImage(Image.open("2.png").resize((400,300)))
lbl=Label(image=img)
lbl.place(x=0,y=0,relheight=1,relwidth=1)

#tkinter variable is little bit differnt from python variable
# r is a tkinter variable
# r=IntVar()
# r.set(2)#if you do not the value then the default value will be 0.

# def Clicked(value):
#     myLabel = Label(root, text=value)
#     myLabel.pack()

# Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda :Clicked(r.get())).pack()
# Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda :Clicked(r.get())).pack()

# myLabel = Label(root, text=r.get())
# myLabel.pack()
#
# myButton=Button(root,text="Click Me!!",command=lambda :Clicked(r.get())).pack()



Modes=[
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]
pizz=StringVar()
pizz.set("Pepperoni")

for text,mode in Modes:
    Radiobutton(root,text=text,variable=pizz,value=mode,command=lambda :Clicked(pizz.get())).pack(anchor=W,padx=40,pady=5)

def Clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# myLabel = Label(root, text=pizz.get())
# myLabel.pack()

myButton=Button(root,text="Click Me!!",command=lambda :Clicked(pizz.get())).pack()



root.mainloop()