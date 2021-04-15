from tkinter import *
from tkinter import ttk
import pymysql
import mysql.connector

class Student:
    def __init__(self, *args, **kwargs):
        self.root = root
        self.root.title("Student Managment System")
        self.root.geometry("1350x650+0+0")

        title=Label(self.root,text="Studente Managment System",font=("time new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)


        #====================All Variables====================
        self.roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.conatct_var=StringVar()
        self.dob_var=StringVar()



        #================== Manage Frame =====================
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=70,width=470,height=570)

        m_title=Label(Manage_Frame,text="Manage Students",font=("time new roman",30,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)

        #---------------------- Roll No label --------------------------
        lbl_roll=Label(Manage_Frame,text="Roll No:",bg="crimson",fg="white",font=("time new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        self.txt_roll=Entry(Manage_Frame,textvariable=self.roll_No_var,font=("time new roman",15,"bold"),bd=2,relief=GROOVE)
        self.txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        # ----------------------  Name label --------------------------
        lbl_name = Label(Manage_Frame, text="Name:", bg="crimson", fg="white", font=("time new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.txt_name = Entry(Manage_Frame,textvariable=self.name_var ,font=("time new roman", 15, "bold"), bd=2, relief=GROOVE)
        self.txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        # ---------------------- Email label --------------------------
        lbl_email = Label(Manage_Frame, text="Email:", bg="crimson", fg="white", font=("time new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.txt_email = Entry(Manage_Frame,textvariable=self.email_var,font=("time new roman", 15, "bold"), bd=2, relief=GROOVE)
        self.txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        # ---------------------- Gender label --------------------------
        lbl_gender = Label(Manage_Frame, text="Gender:", bg="crimson", fg="white", font=("time new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        self.combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("time new roman", 15, "bold"))
        self.combo_gender['values'] = ("Male","Female","Others")
        self.combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")


        # ---------------------- contact label --------------------------
        lbl_contact = Label(Manage_Frame, text="Contact:", bg="crimson", fg="white", font=("time new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        self.txt_contact = Entry(Manage_Frame,textvariable=self.conatct_var,font=("time new roman", 15, "bold"), bd=2, relief=GROOVE)
        self.txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # ---------------------- D.O.B label --------------------------
        lbl_DOB = Label(Manage_Frame, text="D.O.B:", bg="crimson", fg="white", font=("time new roman", 20, "bold"))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.txt_DOB = Entry(Manage_Frame,textvariable=self.dob_var,font=("time new roman", 15, "bold"), bd=2, relief=GROOVE)
        self.txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # ---------------------- Address label --------------------------
        lbl_address = Label(Manage_Frame, text="Address:", bg="crimson", fg="white", font=("time new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_address = Text(Manage_Frame,width=32,height=4,font=("",10))
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        #----------------------Button Frame -----------------------
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=10,y=500,width=450,height=50)

        add_button=Button(btn_Frame,text="Add",width=9,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        update_button=Button(btn_Frame,text="Update",width=9).grid(row=0,column=1,padx=10,pady=10)
        delete_button=Button(btn_Frame,text="Delete",width=9,command=self.delete_all).grid(row=0,column=2,padx=10,pady=10)
        clear_button=Button(btn_Frame,text="Clear",width=9).grid(row=0,column=3,padx=10,pady=10)









        # ================== Detail Frame =====================
        detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        detail_Frame.place(x=520, y=70, width=800, height=570)

        lbl_search=Label(detail_Frame,text="search by",bg="crimson",fg="white",font=("time new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20)

        combo_search = ttk.Combobox(detail_Frame,width=10,font=("time new roman", 15, "bold"))
        combo_search['values'] = ("Roll No", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_Search=Entry(detail_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        search_button=Button(detail_Frame,text="Search",width=9).grid(row=0,column=3,padx=10,pady=10)
        showAll_button=Button(detail_Frame,text="Show All",width=9).grid(row=0,column=4,padx=10,pady=10)

        #======================Table Frame ================================
        Table_Frame=Frame(detail_Frame,bd=3,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=450)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.xview)
        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("Address", text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("Address",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()

        #add student for my dataBase when you click add button
    def add_student(self):
        con=pymysql.connect(host="Localhost",user="root",password="",database="faresdb")
        #con=pymysql.connect(host="localhost",port=8080,user="root",password="helloworld",database="stm")
        cur=con.cursor()
        cur.execute("insert into Stud values(%s,%s,%s,%s,%s,%s)",(self.roll_No_var.get(),
                    self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.conatct_var.get(),self.dob_var.get()))
        con.commit()
        self.fetch_data()
        con.close()

        #fetch data from Database and show me in my app window
    def fetch_data(self):
        con=pymysql.connect(host="Localhost",user="root",password="",database="faresdb")
        cur=con.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
               self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def delete_all(self):
        self.txt_roll.delete(first=0,last=25)
        self.txt_name.delete(first=0,last=25)
        self.txt_email.delete(first=0, last=25)
        self.txt_contact.delete(first=0, last=25)
        self.txt_DOB.delete(first=0, last=25)
        self.txt_address.delete("1.0","end")


root=Tk()
ob=Student(root)
root.mainloop()