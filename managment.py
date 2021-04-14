from tkinter import *
from tkinter import ttk
class Student:
    def __init__(self, *args, **kwargs):
        self.root = root
        self.root.title("Student Managment System")
        self.root.geometry("1350x650+0+0")

        title=Label(self.root,text="Studente Managment System",font=("time new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)
        #================== Manage Frame =====================
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=70,width=470,height=570)

        m_title=Label(Manage_Frame,text="Manage Students",font=("time new roman",30,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)

        #---------------------- Roll No label --------------------------
        lbl_roll=Label(Manage_Frame,text="Roll No:",bg="crimson",fg="white",font=("time new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_Frame,font=("time new roman",15,"bold"),bd=2,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        # ----------------------  Name label --------------------------
        lbl_name = Label(Manage_Frame, text="Name:", bg="crimson", fg="white", font=("time new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame, font=("time new roman", 15, "bold"), bd=2, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        # ---------------------- Email label --------------------------
        lbl_email = Label(Manage_Frame, text="Email:", bg="crimson", fg="white", font=("time new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(Manage_Frame, font=("time new roman", 15, "bold"), bd=2, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        # ---------------------- Gender label --------------------------
        lbl_gender = Label(Manage_Frame, text="Gender:", bg="crimson", fg="white", font=("time new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame, font=("time new roman", 15, "bold"))
        combo_gender['values'] = ("Male","Female","Others")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")


        # ---------------------- contact label --------------------------
        lbl_contact = Label(Manage_Frame, text="Contact:", bg="crimson", fg="white", font=("time new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(Manage_Frame, font=("time new roman", 15, "bold"), bd=2, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # ---------------------- D.O.B label --------------------------
        lbl_DOB = Label(Manage_Frame, text="D.O.B:", bg="crimson", fg="white", font=("time new roman", 20, "bold"))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_DOB = Entry(Manage_Frame, font=("time new roman", 15, "bold"), bd=2, relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # ---------------------- Address label --------------------------
        lbl_address = Label(Manage_Frame, text="Address:", bg="crimson", fg="white", font=("time new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_address = Text(Manage_Frame,width=32,height=4,font=("",10))
        txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        #----------------------Button Frame -----------------------
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=10,y=500,width=450,height=50)

        add_button=Button(btn_Frame,text="Add",width=9).grid(row=0,column=0,padx=10,pady=10)
        update_button=Button(btn_Frame,text="Update",width=9).grid(row=0,column=1,padx=10,pady=10)
        delete_button=Button(btn_Frame,text="Delete",width=9).grid(row=0,column=2,padx=10,pady=10)
        clear_button=Button(btn_Frame,text="Clear",width=9).grid(row=0,column=3,padx=10,pady=10)









        # ================== Detail Frame =====================
        detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        detail_Frame.place(x=520, y=70, width=800, height=570)


root=Tk()
ob=Student(root)
root.mainloop()