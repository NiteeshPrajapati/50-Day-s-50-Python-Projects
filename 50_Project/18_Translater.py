from tkinter import * 
from tkinter import ttk     
from googletrans import Translator, LANGUAGES

def change(text = "type",src = "English",dest = "Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    translator = Translator()
    translation = translator.translate(text, src=src1, dest=dest1)
    return translation.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0,END)
    textget = change(text = msg,src = s,dest = d)
    Dest_txt.delete(1.0,END)
    Dest_txt.insert(END,textget)


root  = Tk()
root.title("Translator")
root.geometry("500x1000")    
root.config(bg="sky blue")


lab_text = Label(root, text="Translator", font=("Time New Roman", 40,"bold"),bg="light blue")
lab_text.place(x=100,y=40,height=50,width=300)

lab_text.config(fg="black")
lab_text.pack(pady=10)
frame = Frame(root).pack(side=BOTTOM)

lab_text = Label(root, text="Source TEXT", font=("Time New Roman", 20,"bold"),bg="light yellow")
lab_text.place(x=100,y=100,height=20,width=300)

Sor_txt = Text(frame,font = ("Time New Roman", 20,"bold"),wrap=WORD, bg="light blue", fg="black")
Sor_txt.place(x=10,y=130,height=150,width=480)

list_txt = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value = list_txt)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("English")

button_change = Button(frame,text="Translate",relief=RAISED,command=data,bg="light green",font=("Time New Roman", 20,"bold"))
button_change.place(x=170,y=300,height=40,width=150)

comb_dest = ttk.Combobox(frame,value = list_txt)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("English")

lab_text = Label(root, text="Destination TEXT", font=("Time New Roman", 20,"bold"),bg="light yellow")
lab_text.place(x=100,y=360,height=20,width=300)

Dest_txt = Text(frame,font = ("Time New Roman", 20,"bold"),wrap=WORD, bg="light blue", fg="black")
Dest_txt.place(x=10,y=360,height=150,width=480)

root.mainloop()
