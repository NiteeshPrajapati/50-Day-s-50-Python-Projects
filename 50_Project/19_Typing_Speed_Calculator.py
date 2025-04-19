from time import *
import random as r
def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error+=1
        except:
            error+=1
    return error

def speed_time(start_time,end_time,user_input):
    
    time_taken = end_time - start_time
    time_R = round(time_taken, 2)
    speed = len(user_input) / time_R * 60
    return round(speed)



test =["Hello my Name is Niteesh Hiralal pandit Student of B.tech 3rd year CSE branch.","A Python compiler, like the CPython compiler, is a tool that translates Python code (written in a human-readable form) into mac","Welcome to the world of Python programming!","Python is a high-level, interpreted programming language known for its simplicity and readability.","Python is widely used in web development, data analysis, artificial intelligence, scientific computing, and more."]

if __name__ == "__main__":
   while True:
    ck = input("Do you want to start the typing speed test? (y/n): ")
    if ck == 'y':
       print("......Typing Speed Test......")
       test1 = r.choice(test)
       print("Type the following text as fast as you can:")
       time_1= time()
       testInput=input("Enter:"+test1+"\n")
       time_2 = time()
       print('Speed:',speed_time(time_1,time_2,testInput),"w/sec")
       print('Errors:',mistake(test1,testInput))
    
    elif ck == 'n':
        print("Thank you for using the typing speed test.")
        break   
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        
        