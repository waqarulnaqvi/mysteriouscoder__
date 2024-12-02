# 19 6
from tkinter import *
from PIL import Image,ImageTk
#Almost everything in tkinter is a 2 step process except image in tkinter.

root=Tk()
root.geometry("500x400")
root.title("Frame in tkinter")
root.iconbitmap('jarvis.ico')
img=ImageTk.PhotoImage(Image.open("2.png").resize((400,300)))
lbl=Label(image=img)
lbl.place(x=0,y=0,relheight=1,relwidth=1)
# self.bl.place(x=0, y=0, relwidth=1, relheight=1)

frame=Frame(root,padx=50,pady=50)#inside padding
# frame=LabelFrame(root,padx=50,pady=50)#inside padding


# frame=Frame(root,text="heelo world",padx=50,pady=50)#Error
# frame=LabelFrame(root,text="This is my Frame...",padx=50,pady=50)#Run
#inside padding1
frame.pack(padx=50,pady=50)#outside padding
# frame.grid(row=0,column=0)

#we can use grid system inside the frame means we can rearrange the space of button or label inside the frame.
b=Button(frame,text="Don't Click here").grid(row=0,column=0)
b2=Button(frame,text="Don't Click here").grid(row=1,column=1)


root.mainloop()