name =input("Type your name: ")
print("Hello, " + name + "! Welcome to the Choose Your Own Adventure Game!")

answer = input("You are on a deserted island. You see a plane to your left and a boat to your right. Which one do you choose? Type 'plane' or 'boat' and press 'Enter'.").lower()

if answer == "plane":
    answer = input("You chose the plane. You are now flying over the ocean. The plane starts to shake. Do you want to jump out of the plane or stay in the plane? Type 'jump' or 'stay' and press 'Enter'.").lower()
    if answer == "jump":
        print("You jumped out of the plane and landed in the ocean. You see a boat in the distance. You swim towards the boat and climb aboard. You are safe!")
    elif answer == "stay":
        print("You stayed in the plane. The plane crashes into the ocean. You are now stranded in the middle of the ocean. Game Over!")
    else:
        print("Sorry, I didn't understand that. Please type 'jump' or 'stay' and press 'Enter'.")
elif answer == "boat":
    answer = input("You chose the boat. You are now sailing across the ocean. You see a storm in the distance. Do you want to sail towards the storm or away from the storm? Type 'towards' or 'away' and press 'Enter'.").lower()
    if answer == "towards":
        print("You sailed towards the storm. The storm was too strong and the boat capsized. You are now stranded in the middle of the ocean. Game Over!")
    elif answer == "away":
        print("You sailed away from the storm. The storm passed and you see land in the distance. You sail towards the land and reach safety!")
    else:
        print("Sorry, I didn't understand that. Please type 'towards' or 'away' and press 'Enter'.")
else:
    print("Sorry, I didn't understand that. Please type 'plane' or 'boat' and press 'Enter'.")       