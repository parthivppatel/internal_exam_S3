from tkinter import *
from tkinter import messagebox
import random

root=Tk()
root.geometry("1100x652")

f1=Frame(root,borderwidth=3,relief="solid",width=400,height=400,background="dark blue")
f2=Frame(root,borderwidth=3,relief="solid",width=400,height=400,background="dark blue")
  

#labels
l1=Label(f1,text="First Name:")
l1.place(x=5,y=10)
l2=Label(f1,text="Last Name:")
l2.place(x=5,y=40)
l3=Label(f1,text="Gender:")
l3.place(x=5,y=70)
l4=Label(f1,text="Languages:")
l4.place(x=5,y=100)
l5=Label(f1,text="Email:")
l5.place(x=5,y=130)
l6=Label(f1,text="Address:")
l6.place(x=5,y=160)
l7=Label(f1,text="state:")
l7.place(x=5,y=280)
l8=Label(f1,text="Zip:")
l8.place(x=5,y=310)
l9=Label(f1,text="credit card type:")
l9.place(x=5,y=340)

#variables
fname=StringVar()
lname=StringVar()
gender=StringVar(f1,"1")
ch1=IntVar()
ch2=IntVar()
ch3=IntVar()
languages=IntVar()
Email=StringVar()
Address=StringVar()
st1=StringVar(f1,"1")
zip=StringVar()
credit=StringVar(f1,"1")

#entry
Entry(f1,textvariable=fname,width=30).place(x=120,y=10)
Entry(f1,textvariable=lname,width=30).place(x=120,y=40)
Radiobutton(f1,text="Male",value="male",variable=gender).place(x=120,y=70)
Radiobutton(f1,text="Female",value="Female",variable=gender).place(x=170,y=70)
Checkbutton(f1,text="telugu",onvalue=1,offvalue=0,variable=ch1).place(x=120,y=100)
Checkbutton(f1,text="hindi",onvalue=1,offvalue=0,variable=ch2).place(x=180,y=100)
Checkbutton(f1,text="english",onvalue=1,offvalue=0,variable=ch3).place(x=240,y=100)
Entry(f1,textvariable=Email,width=30).place(x=120,y=130)
Text(f1,width=30,height=6).place(x=120,y=160)
Radiobutton(f1,text="gujarat",value="gujarat",variable=st1).place(x=120,y=280)
Radiobutton(f1,text="rajasthan",value="rajasthan",variable=st1).place(x=190,y=280)
Entry(f1,textvariable=zip,width=30).place(x=120,y=310)
Radiobutton(f1,text="visa",value="visa",variable=credit).place(x=120,y=340)
Radiobutton(f1,text="premium",value="premium",variable=credit).place(x=170,y=340)
 
# scroll=Scrollbar(f1)
# scroll.place(x=120,y=160)
# scroll.config(command=t1)

#submit
def submit():
    #validation 1
    ok=0
    name1=fname.get()
    name2=lname.get()

    if(name1=="" or name2==""):
        messagebox.showerror("name","name is compulsory")
    else:
      for i in range(0,9):
        for j in name1:
            if j==str(i):
               ok=1 
               fname.set("")
        for j in name2:
            if j==str(i):
              ok=1
              lname.set("")

      if ok==1 :
        messagebox.showerror("name" ,"invalid name ")
    
    #validation2
    e=Email.get()
    
    if(e!=""): 
      valid=[]
      for i in e:
        valid.append(i)
    
    
      if "@" not in valid:
        messagebox.showerror("email","please enter valid email")
        Email.set("")
    else:
        messagebox.showerror("email","email is compulsory")

    #validation3
    z=zip.get()
    if(z!=""):
      try:

        num=int(z)
      except:
        messagebox.showerror("zip","invalid zip")
        zip.set("")

    g=gender.get()
    if(g=="1"):
        messagebox.showerror("gender","gender is compulsory")

    #listtbox
    
    values=[]
    values.append(name1)
    values.append(name2)
    values.append(g)
    values.append(e)

    for i in values:
        lb.insert(END,i)


def delete():
    lb.delete(0,END)

def theme():
    num=random.choice(range(0,3))
    if(num==1):
     f1.config(background="cyan")
     f2.config(background="cyan")
    else:
     f1.config(background="blue")
     f2.config(background="blue")

Button(root,text="insert",width=10,command=submit).place(relx=0.4,rely=0.2,x=40)
Button(root,text="delete",width=10,command=delete).place(relx=0.4,rely=0.3,x=40)
Button(root,text="theme",width=10,command=theme).place(relx=0.4,rely=0.4,x=40)

l1=Label(f2,text="billling records",bg="grey",width=40,height=3,font=("arial",12,"bold")).place(x=0,y=0)

lb=Listbox(f2)
lb.place(x=0,y=60,width=400)
f1.place(x=25,y=25)
f2.place(x=650,y=25)

root.mainloop()