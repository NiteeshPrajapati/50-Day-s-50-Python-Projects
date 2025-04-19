from tkinter import *
from speedtest import * # pip install speedtest-cli
import os

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_best_server()
    download_speed = str(round(sp.download() / (10**6),3))+" Mbps"  # Convert to Mbps
    upload_speed = str(round(sp.upload() / (10**6),3))+" Mbps"  # Convert to Mbps
    lab_down.config(text = download_speed)
    lab_up.config(text = upload_speed)

sp = Tk()
sp.title(" Internet Speed Test ")
sp.geometry("400x600")
sp.config(bg="lightblue")

lab = Label(sp, text="Internet Speed Test", font=("Arial", 20,"bold"),fg="black",bg = "lightblue")
lab.place(x=60, y=40,height=50,width=300)

lab = Label(sp, text="Downlod Speed", font=("Arial", 20,"bold"), bg="lightyellow",fg="black")
lab.place(x=60, y=130,height=50,width=300)

lab_down = Label(sp, text="00", font=("Arial", 20,"bold"), bg="lightyellow",fg="black")
lab_down.place(x=60, y=200,height=50,width=300)

lab_up = Label(sp, text="Upload Speed", font=("Arial", 20,"bold"), bg="lightyellow",fg="black")
lab_up.place(x=60, y=290,height=50,width=300)

lab = Label(sp, text="00", font=("Arial", 20,"bold"), bg="lightyellow",fg="black")
lab.place(x=60, y=360,height=50,width=300)

button = Button(sp,text = "CHECK Speed", font=("Arial", 20,"bold"),relief=RAISED, bg="lightgreen",fg="black",command=speedcheck)
button.place(x=60, y=460,height=50,width=300)
sp.mainloop()