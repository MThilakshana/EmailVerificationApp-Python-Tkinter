from tkinter import *

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
                 cursor='hand2')
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
                 cursor='hand2')
verifybtn.pack(fill=X,padx=130,pady=10)

exitlabel = Button(root,
                 text="Exit",
                 font=("Times 8"),
                 fg='White',
                 bg='#167000',
                 border=0,
                 cursor='hand2')
exitlabel.pack(fill=X,padx=160)




root.mainloop()