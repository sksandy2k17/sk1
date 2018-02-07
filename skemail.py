import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login("santhosh.17cs@cmr.edu.in", "8*****"*)



#Send the mail
msg = "Hello!"


server.sendmail("santhosh.17cs@cmr.edu.in", "srrajesh113@gmail.com", msg)

