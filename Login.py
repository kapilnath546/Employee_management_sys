from customtkinter import *
from PIL import Image
from tkinter import messagebox
def login():
    if usernameEntry.get()=='':
        messagebox.showerror('Error','Please fill the Username')
    if passwordEntry.get() == '':
        messagebox.showerror('Error', 'Please fill the Password')
    elif usernameEntry.get()=='kapil' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Invalid credentials')



root=CTk()
root.geometry('930x478+100+100')
root.resizable(0,0)
root.title('Login Page')
image=CTkImage(Image.open('cover.jpg'),size=(1030,478))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text='Employee Management System',bg_color='#8396E2',font=('Foudy Old Style',20,'bold'),text_color='white',width=350)
headinglabel.place(x=20,y=100)

usernameEntry=CTkEntry(root,placeholder_text='Enter Your Username',width=190,bg_color='#8396E2')
usernameEntry.place(x=90,y=140)

passwordEntry=CTkEntry(root,placeholder_text='Enter Your Password',width=190,bg_color='#8396E2',show='*')
passwordEntry.place(x=90,y=180)

loginButton=CTkButton(root,text='Login',bg_color='#8396E2',cursor='hand2',command=login)
loginButton.place(x=90,y=220)




root.mainloop()