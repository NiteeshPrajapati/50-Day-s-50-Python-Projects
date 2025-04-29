from tkinter import *
from tkinter import ttk
import requests

def data_get():
   city = city_name.get()
   data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=1403a27b9cc35362260a69bfee76637c").json()
# This code imports the required modules for creating a GUI application using Tkinter and making HTTP requests using the requests module.
# It defines a function called data_get that retrieves weather data from an API based on the city name entered by the user.
   Wb_lable1.config(text = data['weather'][0]['main'])
   W_lable1.config(text = data['weather'][0]['description'])
   temp_lable1.config(text = str(int(data['main']['temp']-273.15))) + "°C"
   Pressure_lable1.config(text = str(int(data['main']['pressure']))) 




win = Tk()
# This code creates a Tkinter window for a weather application.
# The window is created using the Tk() class from the tkinter module.
win.title("Weather Application")
win.geometry("500x570")
win.config(bg="black")
name_lable = Label(win, text="Weather Application", font=('Times New Roman', 30, 'bold'), bg="black", fg="white")
# This code creates a label with the text "Weather Application" using the Label class from the tkinter module.
# The label is styled with a font, background color, and text color.
name_lable.place(x=25,y=50, width=450, height=100)
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
# This code creates a list of city names for the weather application.
com = ttk.Combobox(win, font=('Times New Roman', 20, 'bold'), state="readonly", values=list_name,textvariable=city_name)
# This code creates a read-only combobox using the ttk.Combobox class from the tkinter module.
# The combobox is styled with a font.
# The values for the combobox are set to the list of city names.
com.place(x=25, y=120, width=450, height=50)

W_lable = Label(win, text="Weather climate:", font=('Times New Roman', 20), bg="black", fg="white")
W_lable.place(x=25, y=260, width=200, height=40)
W_lable1 = Label(win, text="", font=('Times New Roman', 20), bg="black", fg="white")
W_lable1.place(x=250, y=260, width=200, height=40)

Wb_lable = Label(win, text="Weather Discription:", font=('Times New Roman', 20), bg="black", fg="white")
Wb_lable.place(x=25, y=330, width=230, height=40)
Wb_lable1 = Label(win, text="", font=('Times New Roman', 20), bg="black", fg="white")
Wb_lable1.place(x=250, y=330, width=230, height=40)

temp_lable = Label(win, text="Temprature:", font=('Times New Roman', 20), bg="black", fg="white")
temp_lable.place(x=25, y=400, width=180, height=40)
temp_lable1 = Label(win, text="", font=('Times New Roman', 20), bg="black", fg="white")
temp_lable1.place(x=250, y=400, width=180, height=40)

Pressure_lable = Label(win, text="Pressure:", font=('Times New Roman', 20), bg="black", fg="white")
Pressure_lable.place(x=25, y=470, width=180, height=40)
Pressure_lable1 = Label(win, text="", font=('Times New Roman', 20), bg="black", fg="white")
Pressure_lable1.place(x=250, y=470, width=180, height=40)



Done_button = Button(win,text="Done", font=('Times New Roman', 20, 'bold'), bg="blue", fg="white",command=data_get)
# This code creates a button with the text "Done" that, when clicked, will call the data_get function to retrieve weather data.
Done_button.place(x=200, y=190, width=100, height=50)




win.mainloop() 