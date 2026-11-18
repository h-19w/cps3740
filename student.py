from tkinter import *


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x600+1+1")
        self.root.title("Welcome to my first application")
        self.root.configure(bg="lightblue")
        self.root.resizable(False, False)
        title = Label(self.root, 
                      text="[Student Information]",
                        font=("times new roman", 30, "bold"), 
                        bg="lightpink"
                        )
        title.pack(fill=X)
root=Tk()
ob=Student(root)
root.mainloop()

