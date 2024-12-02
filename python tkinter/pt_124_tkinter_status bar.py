from tkinter import *
from PIL import Image,ImageTk #pip install pillow
# pil stands for python image library
# Everything in tkinter is a two step process
# But Image is a three step process.
root=Tk()
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    if image_number==5:
        image_number-=1

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    my_label.grid(row=0,column=0,columnspan=3)
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1)).grid(row=1, column=0)
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1)).grid(row=1, column=2)

    if image_number==4:
        # button_forward=Button(root,text=">>",state=DISABLED).grid(row=1,column=2
        button_forward = Button(root, text=">>", command=lambda: forward(image_number:=1)).grid(row=1, column=2)
    status =Label(root,bd=1,borderwidth=3,relief=SUNKEN,anchor=W,text=f"Image {image_number} of {len(image_list)}").grid(sticky=W+E,pady=10,row=2,column=0,columnspan=3)

def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    my_label.grid(row=0,column=0,columnspan=3)
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1)).grid(row=1, column=0)
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1)).grid(row=1, column=2)
    if image_number==0:
        image_number+=1

    if image_number==1:
        # button_back = Button(root, text="<<",state=DISABLED, command=back).grid(row=1, column=0)
        button_back = Button(root, text="<<", command=lambda: back(image_number:=4)).grid(row=1, column=0)

    status =Label(root,bd=1,borderwidth=3,relief=SUNKEN,anchor=W,text=f"Image {image_number} of {len(image_list)}").grid(sticky=W+E,pady=10,row=2,column=0,columnspan=3)



root.geometry("500x430")
root.title("jarvis ai")
root.iconbitmap('jarvis.ico')

my_img1=ImageTk.PhotoImage(Image.open("jarvis images//jarvisimage1.jpg").resize((500,350)))
my_img2=ImageTk.PhotoImage(Image.open("jarvis images//jarvisimage2.webp").resize((500,350)))
my_img3=ImageTk.PhotoImage(Image.open("jarvis images//jarvisimage3.jpg").resize((500,350)))
my_img4=ImageTk.PhotoImage(Image.open("jarvis images//jarvisimage4.jpg").resize((500,350)))

image_list=[my_img1,my_img2,my_img3,my_img4]

status =Label(root,bd=1,borderwidth=3,relief=SUNKEN,anchor=W,text=f"Image {1} of {len(image_list)}").grid(sticky=W+E,pady=10,row=2,column=0,columnspan=3)

my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

# button_back=Button(root,text="<<",command=back,state=DISABLED).grid(row=1,column=0)
button_back = Button(root, text="<<", command=lambda: back(4)).grid(row=1, column=0)
button_exit=Button(root,text="Exit Program",command=root.quit).grid(row=1,column=1)
button_forward=Button(root,text=">>",command=lambda :forward(2)).grid(row=1,column=2)


root.mainloop()


# 23 52
# 24 23