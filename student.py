from tkinter import *
from tkinter import ttk


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

         ## variables 
        self.id_var = StringVar()
        self.stidentid_var = StringVar()
        self.stname_var = StringVar()
        self.gender_var = StringVar()
        self.email_var = StringVar()
        self.delete_var = StringVar()

        ## Manage Frame
        Manage_Frame = Frame(self.root, bg= "white")
        Manage_Frame.place(x=1035, y=39, width=220, height=350)

        ## Manage Frame Labels and Entries
        lbl_id = Label(Manage_Frame, text="ID", bg="white")
        lbl_id.pack()
        id_entry = Entry(Manage_Frame, bg="lightgray",justify=CENTER, bd =2, textvariable=self.id_var)
        id_entry.pack()

        lbl_name = Label(Manage_Frame, text="Name", bg="white")
        lbl_name.pack()
        name_entry = Entry(Manage_Frame, bg="lightgray",justify=CENTER, bd =2, textvariable=self.stname_var)
        name_entry.pack()

        lbl_studentid = Label(Manage_Frame, text="Student ID", bg="white")
        lbl_studentid.pack()
        studentid_entry = Entry(Manage_Frame, bg="lightgray",justify=CENTER, bd =2, textvariable=self.stidentid_var)
        studentid_entry.pack()

        lbl_gender = Label(Manage_Frame, text="Gender", bg="white")
        lbl_gender.pack()
        gender_entry = ttk.Combobox(Manage_Frame, justify=CENTER, textvariable=self.gender_var)
        gender_entry['values'] = ("Male", "Female", "Other")
        gender_entry.pack()

        lbl_email = Label(Manage_Frame, text="Email", bg="white")
        lbl_email.pack()
        email_entry = Entry(Manage_Frame, bg="lightgray", bd = '2', justify=CENTER, textvariable=self.email_var)
        email_entry.pack()

        lbl_delete = Label(Manage_Frame, text="Delete Student Data", fg="red")
        lbl_delete.pack()
        delete_entry = Entry(Manage_Frame, bd = '2', justify=CENTER, textvariable=self.delete_var)
        delete_entry.pack()


        ### Button Frame
        btn_frame = Frame(self.root, bg="white")
        btn_frame.place(x=1035, y=380, width=220, height=350)
        title = Label(btn_frame, text="[controls]", font=("times new roman", 20, "bold"), bg="forestgreen", fg="white")
        title.pack()


        add_btn = Button(btn_frame, text="Add Record", fg = "Orange")
        add_btn.place(x=33, y=30, width=150, height=33)

        delete_btn = Button(btn_frame, text="Delete Record", fg = "red")
        delete_btn.place(x=33, y=60, width=150, height=33)

        update_btn = Button(btn_frame, text="Update Record", fg = "blue")
        update_btn.place(x=33, y=90, width=150, height=33)

        exit_btn = Button(btn_frame, text="Exit", fg = "black")
        exit_btn.place(x=33, y=120, width=150, height=33)

        ## search Frame
        Search_Frame = Frame(self.root, bg="white")
        Search_Frame.place(x=1, y=40, width=1034, height=50)

        lbl_search = Label(Search_Frame, text="Search", bg="white")
        lbl_search.grid(row=0, column=0, padx=10, pady=10)

        combo_search = ttk.Combobox(Search_Frame, justify=CENTER)
        combo_search['values'] = ("ID", "Name", "Student ID", "Gender", "Email")
        combo_search.grid(row=0, column=1, padx=10)

        lbl_search_entry = Entry(Search_Frame, bg="lightgray", bd = '2')
        lbl_search_entry.grid(row=0, column=2, padx=10)

        search_btn = Button(Search_Frame, text="Search", fg = "blue")
        search_btn.grid(row=0, column=3, padx=10)

        details_Frame = Frame(self.root, bg="white")
        details_Frame.place(x=1, y=90, width=1034, height=500)

        

root=Tk()
ob=Student(root)
root.mainloop()
