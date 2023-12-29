from tkinter import *
from tkinter import messagebox
import random
import smtplib

#define exit button
def exitwindow():
    result = messagebox.askyesno("Confirmation", "Do you want to exit?")
    if result:
        root.destroy()
        
#send otp code
def sendotp():
    email = "edumaster010@gmail.com"
    recevermail = str(emailEntry.get())

    subject = "Email Verification"
    message = "Hi,\n\nYour One-Time Passcode (OTP) is: {}.\nPlease use it to complete account verification.\n\nBest,\nRed Line Softwares".format(otpnumber)

    text = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login(email,"trvzssnpkpzthxnb")

    server.sendmail(email,recevermail,text)
    
    messagebox.showinfo("Information","OTP Send Successfully!\nCheck Your Inbox")
    
#check otp
def checkOtp():
    if str(otpnumber) == str(otp.get()):
        messagebox.showinfo("Information","Email Verified Successfully!")
        emailEntry.delete(0,END)
        otp.delete(0,END)
    else:
        messagebox.showinfo("Warning","Invalid Email")
    
    
#generate ram=ndom otp
otpnumber = random.randint(100000,999999)

root = Tk()
root.title("Email Verification System")
root.configure(background='#167000')
root.geometry('400x330')

label = Label(root,
              text="E-mail Verification System",
              font=("Times 20 bold"),
              fg='White',
              bg='#167000'
              )
label.pack(fill=X)

emaillabel = Label(root,
              text="Enter E-mail Address",
              font=("Times 14"),
              fg='White',
              bg='#167000')
emaillabel.pack(fill=X,pady=(30,0))

emailEntry = Entry(root,
              font=("Times 14"),
              bg='#9AEB87',
              fg='Black',
              width=20,
              justify='center')
emailEntry.pack(fill=X,padx=35)

sendbtn = Button(root,
                 text="Send OTP",
                 font=("Times 14 bold"),
                 cursor='hand2',
                 command=sendotp)
sendbtn.pack(fill=X,padx=130,pady=10)

otplabel = Label(root,
                 text="Enter OTP",
                 font=("Times 14"),
                 fg='White',
                 bg='#167000')
otplabel.pack(fill=X)

otp = Entry(root,
              font=("Times 14"),
              bg='#9AEB87',
              fg='Black',
              width=20,
              justify='center')
otp.pack(fill=X,padx=35)

verifybtn = Button(root,
                 text="Verify Email",
                 font=("Times 14 bold"),
                 cursor='hand2',
                 command=checkOtp)
verifybtn.pack(fill=X,padx=130,pady=10)

exitlabel = Button(root,
                 text="Exit",
                 font=("Times 8"),
                 fg='White',
                 bg='#167000',
                 border=0,
                 cursor='hand2',
                 command=exitwindow)
exitlabel.pack(fill=X,padx=160)




root.mainloop()