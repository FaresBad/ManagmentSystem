from tkinter import *
from PIL import Image,ImageTk,ImageDraw #pip install pillow
from datetime import *
from tkinter import messagebox
import time
from math import *
import pymysql

class Login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("WELCOME IN MY GUI")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        #=============BackGround Colors==============
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)


        #==================Frames=========================
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="LOGIN HERE", font=("times new roman",30,"bold"),bg="white",fg="#08A3D2")
        title.place(x=250,y=50)
        email=Label(login_frame,text="USERNAME:", font=("times new roman",18,"bold"),bg="white",fg="Red")
        email.place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)

        password=Label(login_frame, text="PASSWORD:", font=("times new roman", 18, "bold"), bg="white",fg="Red")
        password.place(x=250,y=250)
        self.txt_pass = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=250, y=280, width=350, height=35)

        btn_reg=Button(login_frame,cursor="hand2",text="Register new Account?",command=self.register,font=("times new roman", 15),bg="white",bd=0,fg="#B00857")
        btn_reg.place(x=250,y=320)
        btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman", 15, "bold"), bg="white",fg="#B00857")
        btn_login.place(x=250,y=350,width=200,height=35)

        #===============Clock=========================
        self.lbl=Label(self.root,text="Welcome Login Form",font=("times new roman", 25, "bold"), bg="#081923",fg="Red",bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)


    def register(self):
        self.root.destroy()
        import ManagmentSystem.managment

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","The username and password are required!!!")
        else:
            try:
                con = pymysql.connect(host="Localhost", user="root", password="", database="faresdb")
                cur = con.cursor()
                cur.execute("select * from login where ID=%s and password=%s",(self.txt_email.get(),self.txt_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Username and password")
                else:
                    messagebox.showerror("Success", "Welcome")
                con.close()
            except EXCEPTION as es:
                messagebox.showerror("Error", f"Error due to {str(es)}",parent=self.root)


root=Tk()
ob=Login_window(root)
root.mainloop()
