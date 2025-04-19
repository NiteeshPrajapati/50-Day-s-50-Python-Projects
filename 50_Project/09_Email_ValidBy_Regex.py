import re
 
email_condition = "^[a-z]+[[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_Email = input("Enter your Email : ")
if re.search(email_condition,user_Email):
    print("Email is valid")
else:
    print("Email is not valid") 
        