import pyautogui
from tkinter import *

def take_ss():
    print("Taking screenshot...")
    add_Data=entry.get()
    path=add_Data+"\\Screenshot.png"
    print(path)
    # Uncomment the line below to take a screenshot and save it as "screenshot.png"
    # ss = pyautogui.screenshot()
    # ss.save("screenshot.png")

# This code takes a screenshot of the entire screen and saves it as "screenshot.png" in the current working directory.
# The screenshot will be saved in the same directory where this script is located.
# You can change the filename and path as needed.
 
win = Tk()
win.title("Screenshot")
win.geometry("700x400")
win.config(bg="black")
win.resizable(False, False)

entry = Entry(win, font=('Times New Roman',30,'bold'), bg="blue", fg="white")
# This code creates an entry field where the user can type something. The entry field is styled with a font, background color, and text color.
# The entry field is placed at coordinates (100, 50) with a width of 350 and height of 100 pixels.
entry.place(x =20, y = 50, anchor = CENTER, width = 660, height = 70)
# The entry field is not used in the screenshot functionality, but it can be used for other purposes if needed.


button = Button(win, text="Take", font=('Times New Roman',50,'bold'), bg="blue", fg="white", command=take_ss)
# This code creates a button with the text "Take" that, when clicked, will call the take_ss function to take a screenshot.

button.place(x =250, y = 140, anchor = CENTER, width =200, height = 100)


win.mainloop() 