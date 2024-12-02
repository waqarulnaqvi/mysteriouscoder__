from tkinter import *
from PIL import ImageTk, Image
from subprocess import call #we can call another python program in our program
class GUI_AI(Tk):
    def __init__(self):
        super().__init__()
        my_img1 = ImageTk.PhotoImage(Image.open("jarvis images//jarvisimage1.jpg").resize((700, 700)))
        my_img2 = ImageTk.PhotoImage(Image.open("jarvis images//jarvisimage2.webp").resize((700, 700)))
        my_img3 = ImageTk.PhotoImage(Image.open("jarvis images//jarvisimage3.jpg").resize((700, 700)))
        my_img4 = ImageTk.PhotoImage(Image.open("jarvis images//jarvisimage4.jpg").resize((700, 700)))

        self.imagelist = [my_img1, my_img2, my_img3, my_img4]
        self.i = 0
        self.changeimage()

    def open_my_file(self):
        call(["python","jarvis_ai.py"])


    def changeimage(self):#using grid system
        self.bl = Label(self, image=self.imagelist[self.i])
        self.bl.place(x=0, y=0, relwidth=1, relheight=1)

        Label(self, text="What jarvis can do?", relief=SUNKEN,bd=3,borderwidth=3,font="lucida 20 bold", fg="white", bg="green",cursor="man").grid(row=0, column=0,padx=90, pady=20)

        Label(self, text="1)Open youtube", font="lucida 15 bold", fg="white", cursor="spider",bg="red",relief=SUNKEN,bd=3,borderwidth=3).grid(row=1, column=0, padx=5)

        Label(self, text="2)Open linkedin", font="lucida 15 bold", fg="white",cursor="spider",relief=SUNKEN ,bg="red",bd=3,borderwidth=3).grid(row=2, column=0, pady=5)

        Label(self, text="3)Open facebook",cursor="spider",relief=SUNKEN, font="lucida 15 bold", fg="white", bg="red",bd=3,borderwidth=3).grid(row=3, column=0, pady=5)

        Label(self,relief=SUNKEN, text="4)Open google",cursor="spider", font="lucida 15 bold", fg="white", bg="red",bd=3,borderwidth=3).grid(row=4, column=0, pady=5)

        Label(self, relief=SUNKEN,text="5)Open stackoverflow",bd=3,cursor="spider",borderwidth=3, font="lucida 15 bold", fg="white", bg="red").grid(row=5, column=0,pady=5)

        Label(self, relief=SUNKEN,text="6)Open code",cursor="spider", font="lucida 15 bold", fg="white", bg="red",bd=3,borderwidth=3).grid(row=6, column=0, pady=5)

        Label(self,relief=SUNKEN, text="7)Open music", cursor="spider",font="lucida 15 bold", fg="white",bd=3,borderwidth=3, bg="red").grid(row=7, column=0, pady=5)

        Label(self, relief=SUNKEN,text="8)Send mail",cursor="spider",bd=3,borderwidth=3, font="lucida 15 bold", fg="white", bg="red").grid(row=8, column=0, pady=5)

        Label(self,relief=SUNKEN, text="9)Tell current time",cursor="spider",bd=3,borderwidth=3, font="lucida 15 bold", fg="white", bg="red").grid(row=9, column=0, pady=5)

        Label(self,relief=SUNKEN, text="10)Search in Wikipedia",cursor="spider",bd=3,borderwidth=3, font="lucida 15 bold", fg="white", bg="red").grid(row=10, column=0, pady=5)

        self.i +=  1
        if self.i == 4:
            self.i = 0
        self.bl.after(300, self.changeimage)


if __name__ == "__main__":
    jarvis = GUI_AI()
    jarvis.geometry("500x500")
    jarvis.wm_iconbitmap(r"jarvis images//jarvis.ico")
    jarvis.title("Jarvis A.I")
    mainloop()




