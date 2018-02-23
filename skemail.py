import smtplib                                      #importing smtp from library
server = smtplib.SMTP('smtp.gmail.com', 587)        #to access gmail 
server.starttls()                                   # to start gmail with security

server.login("santhosh.17cs@cmr.edu.in", "8*****"*) #login to account



#Send the mail 
msg = "Hello!"                                      #message


server.sendmail("santhosh.17cs@cmr.edu.in", "srrajesh113@gmail.com", msg)    #to send mail

