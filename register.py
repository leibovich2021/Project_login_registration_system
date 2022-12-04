from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import  pymysql
############functions
def clear():
    entryfirstname.delete(0,END)
    entrylastname.delete(0,END)
    entrycontact.delete(0,END)
    entryEmail.delete(0,END)
    entryanswer.delete(0,END)
    entrypassword.delete(0,END)
    entryconfirmpassword.delete(0,END)
    comboquestion.delete(0,END)
    check.set(0)




def register():
    if entryfirstname.get()=='' or entrylastname.get()==''  or entrycontact.get()=='' or entryEmail.get()=='' or \
        entrypassword.get()=='' or entryconfirmpassword.get()=='' or comboquestion.get()=='Select' or \
        entryanswer.get()=='':
        messagebox.showerror("Error",'All Field are Required')

    elif entrypassword.get()!=entryconfirmpassword.get():
        messagebox.showerror("Error","Password Mismatch")

    elif check.get()==0:
        messagebox.showerror("Error", "please agree to our terms and consitions")
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='denis1994',database='login_user')
            cur=con.cursor()
            cur.execute("select * from members where email=%s", entryEmail.get())
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exists")

            else:
                cur.execute("insert into members(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",(entryfirstname.get(),entrylastname.get(),entrycontact.get(),entryEmail.get(),comboquestion.get(),entryanswer.get(),entrypassword.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Registration is Succesfull")
                clear()
        except Exception as e:
            messagebox.showerror('error', f'Error due to {e}')

############endfunctions


root=Tk()

root.geometry('1350x710+220+10')
root.title("Registrarion Leibovich Users")

bgimage=PhotoImage(file='my_Image.png')
bgLabel=Label(root, image=bgimage)
bgLabel.place(x=130,y=60)

registerFrame=Frame(root,width=650,height=650)
registerFrame.place(x=630,y=30)

titleLabel=Label(registerFrame,text="Welcome To Leibovich Team", font=('arial',22,"bold"))
titleLabel.place(x=20,y=5)

firstnameLabel=Label(registerFrame,text="First Name",font=("times new roman",18,"bold"))
firstnameLabel.place(x=20,y=80)
entryfirstname=Entry(registerFrame, font=('times new roman',18))
entryfirstname.place(x=20,y=115)

lastnameLabel=Label(registerFrame,text="Last Name",font=("times new roman",18,"bold"),fg="gray20")
lastnameLabel.place(x=370,y=80)
entrylastname=Entry(registerFrame, font=('times new roman',18),bg='white')
entrylastname.place(x=370,y=115)

contactLabel=Label(registerFrame,text="Contact",font=("times new roman",18,"bold"),fg="gray20")
contactLabel.place(x=20,y=200)
entrycontact=Entry(registerFrame, font=('times new roman',18),bg='white')
entrycontact.place(x=20,y=235)

emailLabel=Label(registerFrame,text="Email",font=("times new roman",18,"bold"),fg="gray20")
emailLabel.place(x=370,y=200)
entryEmail=Entry(registerFrame, font=('times new roman',18),bg='white')
entryEmail.place(x=370,y=235)

questionLabel=Label(registerFrame,text="Security Question",font=("times new roman",18,"bold"),fg="gray20")
questionLabel.place(x=20,y=320)

comboquestion=ttk.Combobox(registerFrame,font=("times new roman",16),state="readonly")
comboquestion['values']=('Select','Your Firts Pet Name?','Your Birth Place?','Your Best Frind Name?','Your Favorite Teacher?','Your Favorite Hobby?')
comboquestion.place(x=20,y=355)
comboquestion.current(0)

answerLabel=Label(registerFrame,text="Answer",font=("times new roman",18,"bold"),fg="gray20")
answerLabel.place(x=370,y=320)
entryanswer=Entry(registerFrame, font=('times new roman',18),bg='white')
entryanswer.place(x=370,y=355)


passwordLabel=Label(registerFrame,text="Password",font=("times new roman",18,"bold"),fg="gray20")
passwordLabel.place(x=20,y=440)
entrypassword=Entry(registerFrame, font=('times new roman',18),bg='white')
entrypassword.place(x=20,y=475)


confirmpasswordLabel=Label(registerFrame,text="Confirm Password",font=("times new roman",18,"bold"),fg="gray20")
confirmpasswordLabel.place(x=370,y=440)
entryconfirmpassword=Entry(registerFrame, font=('times new roman',18),bg='white')
entryconfirmpassword.place(x=370,y=475)

check=IntVar()
checkButton=Checkbutton(registerFrame,text="I Agree All The Terms & Conditions",onvalue=1,offvalue=0,variable=check,font=("times new roman" , 14,"bold"))
checkButton.place(x=20,y=530)


buttonimage=PhotoImage(file="register.png")
registerButton=Button(registerFrame,image=buttonimage,bd=0,cursor='hand2',command=register)
registerButton.place(x=250,y=580)


loginimage=PhotoImage(file="login.png")
loginButton=Button(root,image=loginimage,bd=0,bg='gold',cursor='hand2')
loginButton.place(x=170,y=540)


root.mainloop()