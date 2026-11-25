from tkinter import *
from tkinter import ttk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1250x600+100+100')
        self.root.title('Welcome to my first application')
        self.root.configure(background="silver")
        self.root.resizable(False, False)

        title = Label(
            self.root,
            text='[Student Information]',
            bg="yellow",
            font=('monospace', 14),
            fg='black'
        )
        title.pack(fill=X)

        self.id_var=StringVar()
        self.stid_var=StringVar()
        self.stname_var=StringVar()
        self.gender_var=StringVar()
        self.email_var=StringVar()
        self.del_var=StringVar()

        Manage_Frame= Frame(self.root, bg='white')
        Manage_Frame.place(x=1050, y=30, width=210, height=400)
        lbl_ID=Label(Manage_Frame, text='ID', bg='white')
        lbl_ID.pack()
        ID_Entry=Entry(Manage_Frame, bg='white', justify='center', bd='2', textvariable=self.id_var)
        ID_Entry.pack()

        lbl_Name=Label(Manage_Frame, bg='white', text='Student Name')
        lbl_Name.pack()
        Name_Entry=Entry(Manage_Frame, justify='center', bd='2', textvariable=self.stname_var)
        Name_Entry.pack()

        lbl_StID=Label(Manage_Frame, bg='white', text='Student_ID')
        lbl_StID.pack()
        StID_Entry=Entry(Manage_Frame, bg='white', bd='2', textvariable=self.stid_var)
        StID_Entry.pack()

        lbl_Gender=Label(Manage_Frame, bg='white', text='Gender')
        lbl_Gender.pack()
        Combo_Gender=ttk.Combobox(Manage_Frame, textvariable=self.gender_var)
        Combo_Gender['value']=('Male', "Female")
        Combo_Gender.pack()

        lbl_Email=Label(Manage_Frame, bg='white', text='Email')
        lbl_Email.pack()
        Email_Entry=Entry(Manage_Frame, bg='white', bd='2', justify='center', textvariable=self.email_var)
        Email_Entry.pack()

        lbl_delete=Label(Manage_Frame, bg='white', text='Delete Student Data', fg='red')
        lbl_delete.pack()
        delete_Entry=Entry(Manage_Frame, bd='2', justify='center', textvariable=self.del_var)
        delete_Entry.pack()

        #---------Button frame-------------
        btn_Frame=Frame(self.root, bg='white')
        btn_Frame.place(x=1050, y=400, width=210, height=253)
        title=Label(btn_Frame, text='Controls', font=('Deco', 14), fg='red', bg='#1AAECB')
        title.pack()

        add_btn=Button(btn_Frame, text='Add Record', bg='Orange')
        add_btn.place(x=33, y=30, width=150, height=33)

        del_btn=Button(btn_Frame, text='Delete Record', bg='yellow')
        del_btn.place(x=33, y=65, width=150, height=33)

        update_btn=Button(btn_Frame, text='Update Record', bg='white')
        update_btn.place(x=33, y=100, width=150, height=33)

        Clear_btn=Button(btn_Frame, text='Clear Record', bg='black', fg='white')
        Clear_btn.place(x=33, y=135, width=150, height=33)

        Exit_btn=Button(btn_Frame, text='Exit', bg='green', command=root.quit)
        Exit_btn.place(x=33, y=170, width=150, height=33)

        #------------
        search_Frame=Frame(self.root, bg="#EAC19E")
        search_Frame.place(x=1, y=30, width=1048, height=50)

        lbl_search=Label(search_Frame, text='Search', bg='white', width=8)
        lbl_search.place(x=1, y=12)

        combo_search=ttk.Combobox(search_Frame, justify='right')
        combo_search['value']=['id', 'stid', 'stname', 'email', 'phone']
        combo_search.place(x=95, y=12, width=100, height=25)

        search_Entry=Entry(search_Frame, justify='center', bg="white")
        search_Entry.place(x=210, y=12, width=180, height=25)

        search_btn = Button(search_Frame, text='Search', bg='red', fg='white')
        search_btn.place(x=405, y=12, width=80, height=25)

        #--------------display records
        Details_Frame=Frame(self.root, bg="white")
        Details_Frame.place(x=1, y=82, width=1048, height=600)
        Scroll_X=Scrollbar(Details_Frame, orient=HORIZONTAL)
        Scroll_Y=Scrollbar(Details_Frame, orient=VERTICAL)

        self.Student_table=ttk.Treeview(Details_Frame, 
        columns=('ID', 'Student Name', 'Student ID', 'Gender', 'Email', 'Phone'),
        xscrollcommand=Scroll_X,
        yscrollcommand=Scroll_Y)

        self.Student_table.place(x=1, y=1, width=1048, height=590)
        Scroll_X.pack(side=BOTTOM, fill=X)
        Scroll_Y.pack(side=BOTTOM, fill=Y)

        Scroll_X.config(command=self.Student_table.xview)
        Scroll_Y.config(command=self.Student_table.yview)
    
        self.Student_table['show']='headings'
        self.Student_table.heading('ID', text='ID')
        self.Student_table.heading('Student Name', text='Student Name')
        self.Student_table.heading('Student ID', text='Student ID')
        self.Student_table.heading('Gender', text='Gender')
        self.Student_table.heading('Email', text='Email')
        self.Student_table.heading('Phone', text='Phone')

        

root = Tk()
ob = Student(root)
root.mainloop()