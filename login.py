from tkinter import *

def btn1():
    username=txtUsername.get()
    password=txtPassword.get()
    myfile=open("username.txt","r")
    alldata=myfile.readlines()

    for x in alldata:
        linedata=x.split(",")
        if username==linedata[0] and password==linedata[1]:
            lbl3.config(text="Pass")
            lolo=Tk()
            lblLOLO1=Label(lolo,text="haaaaaahaaaaa")
            lblLOLO1.pack()
            lolo.mainloop()



    else:
        lbl3.config(text="Fail")

soso=Tk()


frame1=Frame(soso)
frame2=Frame(soso)
lbl1=Label(frame1,text="Username")
txtUsername=Entry(frame1)
lbl2=Label(frame2,text="Password")
txtPassword=Entry(frame2,show="*")

btn1=Button(soso,text="Add",command=btn1)
lbl3=Label(soso,text=".....")

lbl1.pack()
txtUsername.pack()
frame1.pack()
lbl2.pack()
txtPassword.pack()
frame2.pack()

btn1.pack()
lbl3.pack()

soso.mainloop()
