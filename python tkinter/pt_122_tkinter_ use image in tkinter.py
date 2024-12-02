from tkinter import *
from PIL import Image,ImageTk #pip install pillow
# pil stands for python image library
# Everything in tkinter is a two step process
# But Image is a three step process.
root=Tk()
root.geometry("500x400")
root.title("jarvis ai")
root.iconbitmap('jarvis.ico')
my_img=ImageTk.PhotoImage(Image.open("2.png"))
my_label=Label(image=my_img).pack()

button_quit=Button(root,text="Exit Program",command=root.quit)
button_quit.pack()


root.mainloop()
