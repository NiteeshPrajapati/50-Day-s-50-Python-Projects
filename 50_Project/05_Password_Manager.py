from cryptography.fernet import Fernet 


'''def Write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key  


pwd = input("What is your master password ? "+ "\n")
        
key = load_key() + pwd.encode()
fer = Fernet(key)
        
def view():
     with open("passwords.txt", "a") as f:
        for line in f.readlines():
           # print(line.rstrip())
           data = line.rstrip()
           user, passw = data.split(" | ")
           print("User: ",user,"| Password: ", str(fer.decrypt(passw.encode())))
           
            
def add():
       name = input("What is the name of the account? "+ "\n")
       username = input("What is your username? "+ "\n")
       password = input("What is your password? "+ "\n")
       
       with open("passwords.txt", "a") as f:
           f.write(name + " | " + username + " | " + str(fer.encrypt(password.encode())) + "\n")
while True:
    mode = input ("Would you like to add a new password or view existing ones (view,add)? ").lower()
  
    if mode == "q":
       break

    elif mode == "view":
       view()
    
    elif mode == "add":
        add()
    else:       
        print("Invalid mode selected")
        continue