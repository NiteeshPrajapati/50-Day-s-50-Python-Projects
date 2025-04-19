email= input("Enter your Email : ")# Minimum 6 characters Required (g@g.in, Email_ID@gamil.com)
j,k,d = 0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if ("." in email) and (email.count(".")==1):
                if (email[-4] == ".") ^ (email[-3] == "."):
                    for i in email:
                        if i==i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1 
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue    
                        else:
                            d = 1            
                    if k == 1 or j == 1 or d == 1:
                        print("Email is not valid at 6th position")
                        exit()
                    else:
                        print("Email is valid ")
                        exit()                
                else:
                    print("Email is not valid at 5th position")  
                    exit()  
            else:
                print("Email is not valid at 4th position")
                exit()    
        else:
            print("Email is not valid at 3rd position ")
            exit()
    else:
        print("Email is not valid at 2ns position ")
        exit()
else:
    print("Email is not valid at 1st position ")
    exit()
