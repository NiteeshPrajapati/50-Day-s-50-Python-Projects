from skpy import Skype
import os.path

slogin = Skype("prajaptiniteesh7@gmail.com","Niteesh@2003")

contact = slogin.contacts["live:.cid.2405d0ce58c715aa"]
with open() as f:
    contact.chat.sendFile(f, "Test File", "This is a test file sent using Python")
#contact.chat.sendMsg("Hello World")
#contact.chat.sendFile("C:\\Users\\Niteesh\\Desktop\\test.txt", "Test File", "This is a test file sent using Python")


group = slogin.chats.create(["live:.cid.2405d0ce58c715aa"],"Test Group", "This is a test group created by using Python")
#contact = slogin.contacts["live:.cid.2405d0ce58c715aa"]
#contact.chat.sendMsg("Welcome to my Team guy's. ")
'''for i in contact:
    print(i.name)
    print(i.id)
    print(i.skypeId)
    print(i.displayName)
    print(i.status)
    print(i.phone)
    print(i.countryCode)
    print(i.city)
    print(i.country)
    print(i.state)
    print(i.streetAddress)
    print(i.postalCode)
    print(i.timezone)
    print(i.skypeName)'''
    
    
    
