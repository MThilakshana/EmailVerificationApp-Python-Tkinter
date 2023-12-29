import smtplib

email = "edumaster010@gmail.com"
recevermail = "madurathilakshana999@gmail.com"

subject = "Test mail"
message = "This is a test e mail using python"

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(email,"trvzssnpkpzthxnb")

server.sendmail(email,recevermail,text)

print("Email Send Successfully!")

