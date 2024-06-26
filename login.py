from tkinter import*
from tkinter import ttk
from tkinter import Label, PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition 
from attendance import Attendance
from chatbot import Chatbot

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.new_window = None

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Diya Gupta\Desktop\Login_folder\Images\ribon.png")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Diya Gupta\Desktop\Login_folder\Images\ribon.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #Labels
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #Icon Images
        img2=Image.open(r"C:\Users\Diya Gupta\Desktop\Login_folder\Images\ribon.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\Diya Gupta\Desktop\Login_folder\Images\ribon.png")
        img2=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)


        #Login Button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #Forgot Password button
        forgetpassbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpassbtn.place(x=10,y=370,width=160)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required.")
        elif self.txtuser.get()=="abc" and self.txtpass.get()=="def":
            messagebox.showinfo("Success","Welcome to Real-Time Attendance Tracker!")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="diyagupta1717$$",database="diyadb")
            mycursor=conn.cursor()
            mycursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
            ))

            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("ERROR!","Invalid Username or Password!")
            else:
                open_main=messagebox.askyesno("","Access only Admin?")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #===========================================RESET PASSWORD=======================================================
    def reset_password(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("ERROR!","Select Security Question!",parent=self.root2)
        elif self.txt_security_A.get()=="":
            messagebox.showerror("ERROR!","Please enter the answer!",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("ERROR!","Please enter the new password!",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="diyagupta1717$$",database="diyadb")
            mycursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_A.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("ERROR!","Answer Incorrect!\nPlease enter the correct answer!",parent=self.root2)
            else:
                query=("Update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Information","Your password has been updated.\nYou can login using new password!",parent=self.root2)
                self.root2.destroy()
    #==============================================FORGOT PASSWORD WINDOW======================================================


    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("ERROR!","Please enter the username!")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="diyagupta1717$$",database="diyadb")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            
            if row==None:
                messagebox.showerror("ERROR!","Please enter valid username!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="FORGOT PASSWORD",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Best Friend's Name","Your Nickname")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security_A=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security_A.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_new_password.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset Password",command=self.reset_password,font=("times new roman",15,"bold"),bg="green",fg="white")
                btn.place(x=100,y=290)



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #=======================Variable==============================================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        #======================Background Image===========================================================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Diya Gupta\Desktop\Login_folder\images\login.jpeg")
        
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #=======================Left Image=============================================================
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Diya Gupta\Desktop\Login_folder\images\login.jpeg")
        
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)


        #=============Main Frame=========================
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE!",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #Labels and entries
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email Address",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Best Friend's Name","Your Nickname")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security_A.place(x=370,y=270,width=250)

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #===============================Check button==============================================================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree with the Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #===============Buttons==================================
        img=Image.open(r"C:\Users\Diya Gupta\Desktop\Login_folder\images\register.jpeg")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"C:\Users\Diya Gupta\Desktop\Login_folder\images\loginbutton.jpg")
        img1=img1.resize((200,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)


    #======================FUNCTION DECLARATIONS================================================
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("ERROR!","All fields are required!")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("ERROR!","Confirmed password must be same as password!")
        elif self.var_check.get()==0:
            messagebox.showerror("ERROR!","You must agree with our terms and conditions before logging in!")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="diyagupta1717$$",database="diyadb")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("ERROR!","User already exists!\nPlease try with a different Email ID.")
            else:
                mycursor.execute("Insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("SUCCESS!","User Registered Successfully!")


    def return_login(self):
        self.root.destroy()

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM")

        #Background image

        img=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\Background.png")
        img = img.resize((1530, 790), Image.LANCZOS)
        self.phimg=ImageTk.PhotoImage(img)

        bg_label=Label(self.root, image=self.phimg)
        bg_label.place(x=0,y=0,width=1530,height=790)

        #Title
        title_lbl=Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("Roboto",35,"bold"),fg="black",bg="white")
        title_lbl.place(x=10,y=20,width=1530,height=45)

        #student button
        img1=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\graduated.png")
        img1=img1.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg1=ImageTk.PhotoImage(img1)

        B1=Button(root,image=self.phimg1,command=self.student_details,cursor="hand2")
        B1.place(x=200,y=100,width=220,height=220)

        B_1=Button(root,text="Student Details",command=self.student_details, cursor="hand2",font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_1.place(x=200,y=300,width=220,height=40)


        #=============================Face detection button=================================================================================
        img2=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\facescan.png")
        img2=img2.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg2=ImageTk.PhotoImage(img2)

        B2=Button(root,image=self.phimg2,cursor="hand2",command=self.face_data)
        B2.place(x=500,y=100,width=220,height=220)

        B_2=Button(root,text="Face Detector", cursor="hand2",command=self.face_data,font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_2.place(x=500,y=300,width=220,height=40)


        #==========================Attendance button========================================================================================
        img3=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\attendance1.png")
        img3=img3.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg3=ImageTk.PhotoImage(img3)

        B3=Button(root,image=self.phimg3,cursor="hand2",command=self.attendance_data)
        B3.place(x=800,y=100,width=220,height=220)

        B_3=Button(root,text="Attendance", cursor="hand2",command=self.attendance_data,font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_3.place(x=800,y=300,width=220,height=40)


        #===========================Chat Bot button=========================================================================================
        img4=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\robot.png")
        img4=img4.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg4=ImageTk.PhotoImage(img4)

        B4=Button(root,image=self.phimg4,cursor="hand2",command=self.chatbot)
        B4.place(x=1100,y=100,width=220,height=220)

        B_4=Button(root,text="Chat Bot", cursor="hand2",command=self.chatbot,font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_4.place(x=1100,y=300,width=220,height=40)


        #====================Train Data button============================================================================================
        img5=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\train1.png")
        img5=img5.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg5=ImageTk.PhotoImage(img5)

        B5=Button(root,image=self.phimg5,cursor="hand2",command=self.train_data)
        B5.place(x=200,y=380,width=220,height=220)

        B_5=Button(root,text="Train Data", cursor="hand2",command=self.train_data,font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_5.place(x=200,y=580,width=220,height=40)


        #Photos button
        img6=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\gallery.png")
        img6=img6.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg6=ImageTk.PhotoImage(img6)

        B6=Button(root,image=self.phimg6,cursor="hand2",command=self.open_img)
        B6.place(x=500,y=380,width=220,height=220)

        B_6=Button(root,text="Photos", cursor="hand2",command=self.open_img,font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_6.place(x=500,y=580,width=220,height=40)


        #Developer button
        img7=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\coding2.png")
        img7=img7.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg7=ImageTk.PhotoImage(img7)

        B7=Button(root,image=self.phimg7,cursor="hand2")
        B7.place(x=800,y=380,width=220,height=220)

        B_7=Button(root,text="Developer", cursor="hand2",font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_7.place(x=800,y=580,width=220,height=40)


        #Exit button
        img8=Image.open(r"C:\Users\Diya Gupta\Desktop\Face recognition attendance system\Images\exit.png")
        img8=img8.resize((220,220),Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        self.phimg8=ImageTk.PhotoImage(img8)

        B8=Button(root,image=self.phimg8,cursor="hand2")
        B8.place(x=1100,y=380,width=220,height=220)

        B_8=Button(root,text="Exit", cursor="hand2",font=("roboto",15,"bold"),bg="darkblue",fg="white")
        B_8.place(x=1100,y=580,width=220,height=40)


    def open_img(self):
        os.startfile("data")


    #Function Buttons

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)

    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)

    def chatbot(self):
          self.new_window=Toplevel(self.root)
          self.app=Chatbot(self.new_window)


if __name__=="__main__":
    main()