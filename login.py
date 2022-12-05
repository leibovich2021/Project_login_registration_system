from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
#######################Functions
def reset_password():
    if mailentry.get()=='':
        messagebox.showerror('Error',"please enter email address")
    else:
        con=pymysql.connect(host='localhost', user='root', password='denis1994', database='login_user')
        cur=con.cursor()
        cur.execute("select * from members where email=%s",mailentry.get())
        row=cur.fetchone()
        if row==None:
            messagebox.showerror('Error','Please enter the valid email address')
        else:
            con.close()
            def change_password():
                if securityquesCombo.get()=='Select' or answerEntry.get()=='' or newPassEntry.get()=='':
                    messagebox.showerror('Error','All fields are required')
                else:
                    con=pymysql.connect(host='localhost', user='root', password='denis1994', database='login_user')
                    cur=con.cursor()
                    cur.execute('select * from members where email=%s and question=%s and answer=%s',(mailentry.get(),securityquesCombo.get(),answerEntry.get()))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror('Error','Security Question or Answer is Incorrect')
                    else:
                        cur.execute('update members set password=%s where email=%s', (newPassEntry.get(),mailentry.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo('Seccess','Password is reset,Please login with new password',parent=root2)
                        securityquesCombo.current(0)
                        answerEntry.delete(0,END)
                        newPassEntry.delete(0,END)
                        root2.destroy()
            root2=Toplevel()
            root2.title("Forget Password")
            root2.geometry('470x560+400+60')
            root2.config(bg='white')
            root2.focus_force()
            root2.grab_set()
            forgetLable=Label(root2,text='Forget',font=('times new roman',22,'bold'),bg='white')
            forgetLable.place(x=128,y=10)

            forgetpassLable = Label(root2, text='Password', font=('times new roman', 22, 'bold'), bg='white', fg='green')
            forgetpassLable.place(x=225, y=10)

            securityqueslabel=Label(root2,text="Security Questions",font=("times new roman",19,'bold'),bg="white")
            securityqueslabel.place(x=60,y=220)

            securityquesCombo=ttk.Combobox(root2,font=('times new roman',19,),state='readonly',width=28)
            securityquesCombo['values']=('Select','Your Firts Pet Name?','Your Birth Place?','Your Best Frind Name?','Your Favorite Teacher?','Your Favorite Hobby?')

            securityquesCombo.place(x=60,y=260)
            securityquesCombo.current(0)

            answerLabel=Label(root2,text="Answer",font=("times new roman",19,'bold'),bg='white')
            answerLabel.place(x=60,y=310)
            answerEntry=Entry(root2,font=('times new roman',19),bg='white',width=30)
            answerEntry.place(x=60,y=350)

            newPassLabel = Label(root2, text="New Password", font=("times new roman", 19, 'bold'), bg='white')
            newPassLabel.place(x=60, y=400)
            newPassEntry = Entry(root2, font=('times new roman', 19), bg='white', width=30)
            newPassEntry.place(x=60, y=440)

            changepassButton=Button(root2,text="Change Password",font=('arial',17,'bold'),bg='green',fg='white',cursor='hand2',activebackground='green',activeforeground=
                                    'white',command=change_password)
            changepassButton.place(x=130,y=500)

            root2.mainloop()

def register_window():
    window.destroy()
    import register

def signin():
    if mailentry.get()=='' or passwordentry.get()=='':
        messagebox.showerror("error",'All Fields Are Required')
    else:
        try:

            con = pymysql.connect(host='localhost', user='root', password='denis1994', database='login_user')
            cur=con.cursor()
            cur.execute("select * from members where email=%s and password=%s",(mailentry.get(),passwordentry.get()))
            row=cur.fetchone()

            if row==None:
                messagebox.showerror('error','Invalid Email or Password')
            else:
                messagebox.showinfo('Succses',"Welcome")
                con.close()
        except Exception as a:
            messagebox.showerror('error',f'Error is due to {e}')






##################




window=Tk()

window.geometry('1350x710+220+10')
window.title("login Leibovich Users")

bgloginimage=PhotoImage(file='my_Image.png')
bgloginLabel=Label(window, image=bgloginimage)
bgloginLabel.place(x=130,y=60)

frame=Frame(window,width=650,height=650)
frame.place(x=630,y=30)

titleloginLabel=Label(frame,text="Welcome To Leibovich Team", font=('arial',22,"bold"))
titleloginLabel.place(x=20,y=5)

maillabel=Label(frame,text="Email", font=('arial',22,"bold"))
maillabel.place(x=75,y=150)
mailentry=Entry(frame, font=('arial',22))
mailentry.place(x=250,y=150)


passwordlabel=Label(frame,text="Password", font=('arial',22,"bold"))
passwordlabel.place(x=75,y=270)
passwordentry=Entry(frame, font=('arial',22),show='*')
passwordentry.place(x=250,y=270)



regButton=Button(frame,text="Register New Account?", font=('arial',12),bd=0,bg="white",cursor="hand2",activebackground="white",command=register_window)
regButton.place(x=180,y=500)



forgetButton=Button(frame,text="Forget Password?", font=('arial',12),bd=0,bg="white",activebackground="white",fg='red',activeforeground="red",cursor="hand2",command=reset_password)
forgetButton.place(x=410,y=500)


loginButton=Button(frame,text="Login", font=('arial',18,"bold"),fg="white",bg="gray20",cursor="hand2",activebackground="gray20",activeforeground="white",command=signin)
loginButton.place(x=350,y=380)


window.mainloop()