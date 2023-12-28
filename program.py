from tkinter import *
from tkinter import messagebox
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#define exit button
def exitwindow():
    result = messagebox.askyesno("Confirmation", "Do you want to exit?")
    if result:
        root.destroy()
        
#send otp code
def sendotp():
    sender_email = "edumaster010@gmail.com"
    password = "uifbksavayihbnyy"
    to_email = str(email.get())
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = "Your OTP for Account Verification"
    body = "Hi\nYour One-Time Passcode (OTP) is: {}.\nPlease use it to complete account verification.\nBest,\nRed Line softwares.".format(otpnumber)
    
    message.attach(MIMEText(body,"plain"))
    
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(sender_email,password)
        server.sendmail(sender_email,to_email,message.as_string())
        
    messagebox.showinfo("Information","OTP Send Successfully!\nCheck Your Inbox")
    
#check otp
def checkOtp():
    if str(otpnumber) == str(otp.get()):
        messagebox.showinfo("Information","Email Verified Successfully!")
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

email = Entry(root,
              font=("Times 14"),
              bg='#9AEB87',
              fg='Black',
              width=20,
              justify='center')
email.pack(fill=X,padx=35)

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