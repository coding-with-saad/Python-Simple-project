import smtplib
my_email = "op@gmail.com"
password = "123456789"

connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="op@gmail.com",msg="Hello, this is a test email.")
connection.close()
