import smtplib as a 
ob = a.SMTP("smtp.gmail.com", 587) #Gmail port number is 587
ob.ehlo()
ob.starttls()
ob.login('iloveyousomuchsweeti@gmail.com', ''' Password ''') #Enter your password here
subject = "Sending email using Python"
body = "This is a test email sent using Python"
message = "Subject:{}\n\n{}".format(subject, body)
listofaddress = ["panditniki1234@gmail.com","prajaptiniteesh7@gmail.com"]
ob.sendmail("prajaptiniteesh7@gmail.com",listofaddress,message)
print("send successfully...")
ob.quit()
