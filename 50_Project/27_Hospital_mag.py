from tkinter import *
from tkinter import ttk 
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        
        self.Nameoftable=StringVar()
        self.refrenceno=StringVar()
        self.patientname=StringVar()
        self.address=StringVar()
        self.patientid=StringVar()
        self.doctorname=StringVar()
        self.lotno=StringVar()
        self.issuedate=StringVar()
        self.expdate=StringVar()
        self.dailydose=StringVar()
        self.sideeffect= StringVar()
        self.bloodpressure=StringVar()
        self.bloodsugar = StringVar()
        self.storageadvice = StringVar()
        
        lbltitle = Label(self.root,bd = 20,relief=RIDGE,text = "HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white", font=("time new roman", 50,'bold'))
        lbltitle.pack(side=TOP,fill=X)
        
        ''' ==== Data frame ==== '''
        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)
        
        dataFramLeft=LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("time new roman", 12, 'bold'), text="Patient Information")
        dataFramLeft.place(x=0,y=5,width=980,height=350)   
        
        dataFrameRight=LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("time new roman", 12, 'bold'), text="Prescription")
        dataFrameRight.place(x=990,y=5,width=460,height=350) 
        
        ''' ==== Button Frame ==== '''
        
        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1530,height=70)
        
        ''' ==== Details Frame ==== '''
        DetailsFrame = Frame(self.root,bd =20,relief =RIDGE )
        DetailsFrame.place(x=0,y=600,width=1530,height=200)
        
        ''' ==== DataFrame Left ==== '''
        LblNameTablet = Label(dataFramLeft, text="Names of Tablet:", font=("time new roman", 12, 'bold'), padx=2, pady=6)
        LblNameTablet.grid(row=0, column=0, sticky=W)
        comNameTablet = ttk.Combobox(dataFramLeft, font=("time new roman", 12, 'bold'), width=33,textvariable=self.Nameoftable, state="readonly")
        comNameTablet['value'] = ("Acetaminophen","Adderall","Amitriptyline","Amlodipine","Amoxicillin","Ativan","Atorvastatin","Azithromycin","Benzonatate","Biktarvy","Botox","Brilinta","Bunavail","Buprenorphine","Cephalexin""Ciprofloxacin""Citalopram","Clindamycin","Clonazepam","Cyclobenzaprine","Cymbalta","Doxycycline","Dupixent","Entresto","Entyvio","Farxiga","Fentanyl Patch","Gabapentin","Gemtesa","Humira","Hydrochlorothiazide","Ibuprofen","Imbruvica","Januvia","Jardiance","keytruda","Lexapro","Lisinopril","Lofexidine""Loratadine","Loratadine","Lyrica","Melatonin","Meloxicam","Metformin","Methadone","Methotrexate","Metoprolol","Mounjaro","Naltrexone","Naproxen","Narcan","Nurtec","Omeprazole","Opdivo","Otezla","Ozempic","Pantoprazole","Plan B","Prednisone","Probuphine","Qulipta","Quviviq","Rybelsus","Sublocade","Sunlenca","Tepezza","Tramadol","Trazodone","Viagra","Vraylar","Wegovy","Wellbutrin","Xanax","Yervoy","Zepbound","Zubsolv")
        comNameTablet.grid(row=0, column=1, padx=8, pady=10)
        
        lblRefrence = Label(dataFramLeft, text="Refrence No.", font=("time new roman", 12, 'bold'), padx=2, pady=6)
        lblRefrence.grid(row=1, column=0, sticky=W)
        txtRefrence = Entry(dataFramLeft, font=("time new roman", 12, 'bold'), width=35, textvariable=self.refrenceno)
        txtRefrence.grid(row=1, column=1, padx=8, pady=10)
        
        lblName = Label(dataFramLeft, text="Patient Name:", font=("time new roman", 12, 'bold'), padx=2, pady=6)
        lblName.grid(row=2, column=0, sticky=W)
        txtName = Entry(dataFramLeft, font=("time new roman", 12, 'bold'), width=35,textvariable=self.patientname)
        txtName.grid(row=2, column=1, padx=8, pady=10)
        
        lblAdress = Label(dataFramLeft, text="Address:", font=("time new roman", 12, 'bold'), padx=2, pady=6)
        lblAdress.grid(row=3, column=0, sticky=W)
        txtAdress = Entry(dataFramLeft, font=("time new roman", 12, 'bold'), width=35,textvariable=self.address)
        txtAdress.grid(row=3, column=1, padx=8, pady=10)
        
        lblPatientID = Label(dataFramLeft, text="Patient ID:", font=("time new roman", 12, 'bold'), padx=2, pady=6)
        lblPatientID.grid(row=4, column=0, sticky=W)
        txtPatientID = Entry(dataFramLeft, font=("time new roman", 12, 'bold'), width=35,textvariable=self.patientid)
        txtPatientID.grid(row=4, column=1, padx=8, pady=10)
        
        lblDoctorName = Label(dataFramLeft, text="Doctor Name:", font=("time new roman", 12, 'bold'), padx=2, pady=6)
        lblDoctorName.grid(row=5, column=0, sticky=W)
        txtDoctorName = Entry(dataFramLeft, font=("time new roman", 12, 'bold'), width=35,textvariable=self.doctorname)
        txtDoctorName.grid(row=5, column=1, padx=8, pady=10)
        
        lblLot = Label(dataFramLeft, text="Lot No.:", font=("time new roman", 12, 'bold'), padx=2, pady=6)
        lblLot.grid(row=6, column=0, sticky=W)
        txtLot = Entry(dataFramLeft, font=("time new roman", 12, 'bold'), width=35,textvariable=self.lotno)
        txtLot.grid(row=6, column=1, padx=8, pady=10)
        
        lblissueDate = Label(dataFramLeft, text="Issue Date:", font=("time new roman", 12, 'bold'), padx=2, pady=6)
        lblissueDate.grid(row=0, column=2, sticky=W)    
        txtissueDate = Entry(dataFramLeft, font=("time new roman", 12, 'bold'), width=35,textvariable=self.issuedate)
        txtissueDate.grid(row=0, column=3, padx=8, pady=10)
        
        lblexpDate = Label(dataFramLeft, text="Expiry Date:", font=("time new roman", 12, 'bold'), padx=2, pady=6)
        lblexpDate.grid(row=1, column=2, sticky=W)
        txtExpDate = Entry(dataFramLeft, font=("time new roman", 12, 'bold'), width=35,textvariable=self.expdate)
        txtExpDate.grid(row=1, column=3, padx=8, pady=10)
        
        lblDailyDose = Label(dataFramLeft, text="Daily Dose:", font=("time new roman", 12, 'bold'), padx=2, pady=6)
        lblDailyDose.grid(row=2, column=2, sticky=W)
        txtDailyDose = Entry(dataFramLeft, font=("time new roman", 12, 'bold'), width=35,textvariable=self.dailydose)
        txtDailyDose.grid(row=2, column=3, padx=8, pady=10)
        
        lblSideEffect = Label(dataFramLeft, text="Side Effect:", font=("time new roman", 12, 'bold'), padx=2, pady=6)
        lblSideEffect.grid(row=3, column=2, sticky=W)
        txtSideEffect = Entry(dataFramLeft, font=("time new roman", 12, 'bold'), width=35,textvariable=self.sideeffect)
        txtSideEffect.grid(row=3, column=3, padx=8, pady=10)
        
        lblBloodPressure = Label(dataFramLeft, text="Blood Pressure:", font=("time new roman", 12, 'bold'), padx=2, pady=6)
        lblBloodPressure.grid(row=4, column=2, sticky=W)
        txtBloodPressure = Entry(dataFramLeft, font=("time new roman", 12, 'bold'), width=35,textvariable=self.bloodpressure)
        txtBloodPressure.grid(row=4, column=3, padx=8, pady=10)
        
        lblBloodSugar = Label(dataFramLeft, text="Blood Sugar:", font=("time new roman", 12, 'bold'), padx=2, pady=6)
        lblBloodSugar.grid(row=5, column=2, sticky=W)
        txtBloodSugar = Entry(dataFramLeft, font=("time new roman", 12, 'bold'), width=35,textvariable=self.bloodsugar)
        txtBloodSugar.grid(row=5, column=3, padx=8, pady=10)
        
        lblStorageAdvice = Label(dataFramLeft, text="Storage Advice:", font=("time new roman", 12, 'bold'), padx=2, pady=6)
        lblStorageAdvice.grid(row=6, column=2, sticky=W)
        txtStorageAdvice = Entry(dataFramLeft, font=("time new roman", 12, 'bold'), width=35,textvariable=self.storageadvice)
        txtStorageAdvice.grid(row=6, column=3, padx=8, pady=10)
        
        ''' ==== DataFrame Right ==== '''
        
        self.txtPrescription = Text(dataFrameRight, font=("time new roman", 12, 'bold'), width=40, height=16)
        self.txtPrescription.pack(fill=BOTH, expand=1)
        
        ''' ==== Button Frame ==== '''
        
        btnPrescription = Button(ButtonFrame,command=self.iprecription, text="Prescription", font=("time new roman", 12, 'bold'), bg="black", fg="white", width=24)
        btnPrescription.grid(row=0, column=0)
        
        btnPrescriptionData = Button(ButtonFrame,command=self.iPrescriptionData, text="Prescription Data", font=("time new roman", 12, 'bold'), bg="black", fg="white", width=24)
        btnPrescriptionData.grid(row=0, column=1)
        
        btnUpdate = Button(ButtonFrame,command=self.update, text="Update", font=("time new roman", 12, 'bold'), bg="black", fg="white", width=24)
        btnUpdate.grid(row=0, column=2)
        
        btnDelete = Button(ButtonFrame, text="Delete",command=self.delete, font=("time new roman", 12, 'bold'), bg="black", fg="white", width=24)
        btnDelete.grid(row=0, column=3)
        
        btnClear = Button(ButtonFrame, text="Clear",command=self.clear, font=("time new roman", 12, 'bold'), bg="black", fg="white", width=24)
        btnClear.grid(row=0, column=4)
        
        btnExit = Button(ButtonFrame, text="Exit",command=self.exit, font=("time new roman", 12, 'bold'), bg="black", fg="white", width=24)
        btnExit.grid(row=0, column=5)
        
        ''' ==== Detail table Frame ==== ''' 
        ''' ==== Scroll bar ==== '''
        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)
        
        self.hospital_table = ttk.Treeview(DetailsFrame, column=("nameoftablet","refrenceno","patientname","address","patientid","doctorname","lotno","issuedate","expdate","dailydose","sideeffect","bloodpressure","bloodsugar","storageadvice"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.hospital_table.heading('nameoftablet', text="Name of Table")
        self.hospital_table.heading('refrenceno', text="Refrence No.")
        self.hospital_table.heading('patientname', text="Patient Name")
        self.hospital_table.heading('address', text="Address")
        self.hospital_table.heading('patientid', text="Patient ID")
        self.hospital_table.heading('doctorname', text="Doctor Name")
        self.hospital_table.heading('lotno', text="Lot No.")
        self.hospital_table.heading('issuedate', text="Issue Date")
        self.hospital_table.heading('expdate', text="Exp Date")
        self.hospital_table.heading('dailydose', text="Daily Dose")
        self.hospital_table.heading('sideeffect', text="Side Effect")
        self.hospital_table.heading('bloodpressure', text="BP Count")
        self.hospital_table.heading('bloodsugar', text="BS Count")
        self.hospital_table.heading('storageadvice', text="Storage")
        
        self.hospital_table["show"] = 'headings'
        
        self.hospital_table.column('nameoftablet', width=100)
        self.hospital_table.column('refrenceno', width=100)
        self.hospital_table.column('patientname', width=100)
        self.hospital_table.column('address', width=100)
        self.hospital_table.column('patientid', width=100)
        self.hospital_table.column('doctorname', width=100)
        self.hospital_table.column('lotno', width=100)
        self.hospital_table.column('issuedate', width=100)
        self.hospital_table.column('expdate', width=100)
        self.hospital_table.column('dailydose', width=100)
        self.hospital_table.column('sideeffect', width=100)
        self.hospital_table.column('bloodpressure', width=100)
        self.hospital_table.column('bloodsugar', width=100)
        self.hospital_table.column('storageadvice', width=100)
        
        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
        
        '''=== Functionality declaration ==='''
        
    def iPrescriptionData(self):
        if self.Nameoftable.get()=="" or self.refrenceno.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            try:
                # Try different connection methods
                try:
                    # Method 1: Standard connection
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Test@1234",
                        database="Mydb"
                    )
                except mysql.connector.Error as err:
                    # Method 2: Try without password
                    try:
                        conn = mysql.connector.connect(
                            host="localhost",
                            username="root",
                            database="Mydb"
                        )
                    except mysql.connector.Error as err2:
                        # Method 3: Try with 127.0.0.1 instead of localhost
                        try:
                            conn = mysql.connector.connect(
                                host="127.0.0.1",
                                username="root",
                                password="Test@1234",
                                database="Mydb"
                            )
                        except mysql.connector.Error as err3:
                            # Method 4: Try with 127.0.0.1 and no password
                            conn = mysql.connector.connect(
                                host="127.0.0.1",
                                username="root",
                                database="Mydb"
                            )
                
                my_cursor = conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.Nameoftable.get(),
                    self.refrenceno.get(),
                    self.patientname.get(),
                    self.address.get(),
                    self.patientid.get(),
                    self.doctorname.get(),
                    self.lotno.get(),
                    self.issuedate.get(),
                    self.expdate.get(),
                    self.dailydose.get(),
                    self.sideeffect.get(),
                    self.bloodpressure.get(),
                    self.bloodsugar.get(),
                    self.storageadvice.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Record has been inserted")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error connecting to MySQL: {err}")
                print(f"Detailed error: {err}")
    
    def update(self):
        if self.Nameoftable.get()=="" or self.refrenceno.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            try:
                # Try different connection methods
                try:
                    # Method 1: Standard connection
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Test@1234",
                        database="Mydb"
                    )
                except mysql.connector.Error as err:
                    # Method 2: Try without password
                    try:
                        conn = mysql.connector.connect(
                            host="localhost",
                            username="root",
                            database="Mydb"
                        )
                    except mysql.connector.Error as err2:
                        # Method 3: Try with 127.0.0.1 instead of localhost
                        try:
                            conn = mysql.connector.connect(
                                host="127.0.0.1",
                                username="root",
                                password="Test@1234",
                                database="Mydb"
                            )
                        except mysql.connector.Error as err3:
                            # Method 4: Try with 127.0.0.1 and no password
                            conn = mysql.connector.connect(
                                host="127.0.0.1",
                                username="root",
                                database="Mydb"
                            )
                
                my_cursor = conn.cursor()
                my_cursor.execute("update hospital set nameoftablet=%s,refrenceno=%s,patientname=%s,address=%s,patientid=%s,doctorname=%s,lotno=%s,issuedate=%s,expdate=%s,dailydose=%s,sideeffect=%s,bloodpressure=%s,bloodsugar=%s,storageadvice=%s where nameoftablet=%s",(
                    self.Nameoftable.get(),
                    self.refrenceno.get(),
                    self.patientname.get(),
                    self.address.get(),
                    self.patientid.get(),
                    self.doctorname.get(),
                    self.lotno.get(),
                    self.issuedate.get(),
                    self.expdate.get(),
                    self.dailydose.get(),
                    self.sideeffect.get(),
                    self.bloodpressure.get(),
                    self.bloodsugar.get(),
                    self.storageadvice.get(),
                    self.Nameoftable.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Record has been updated")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error connecting to MySQL: {err}")
                print(f"Detailed error: {err}")
    
    def clear(self):
        self.Nameoftable.set("")
        self.refrenceno.set("")
        self.patientname.set("")
        self.address.set("")
        self.patientid.set("")
        self.doctorname.set("")
        self.lotno.set("")
        self.issuedate.set("")
        self.expdate.set("")
        self.dailydose.set("")
        self.sideeffect.set("")
        self.bloodpressure.set("")
        self.bloodsugar.set("")
        self.storageadvice.set("")
    
    def exit(self):
        exit = messagebox.askyesno("Hospital Management System","Do you want to exit?")
        if exit > 0:
            root.destroy()
            return      
    
    def delete(self):
        if self.Nameoftable.get()=="" or self.refrenceno.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            try:
                # Try different connection methods
                try:
                    # Method 1: Standard connection
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="Test@1234",
                        database="Mydb"
                    )
                except mysql.connector.Error as err:
                    # Method 2: Try without password
                    try:
                        conn = mysql.connector.connect(
                            host="localhost",
                            username="root",
                            database="Mydb"
                        )
                    except mysql.connector.Error as err2:
                        # Method 3: Try with 127.0.0.1 instead of localhost
                        try:
                            conn = mysql.connector.connect(
                                host="127.0.0.1",
                                username="root",
                                password="Test@1234",
                                database="Mydb"
                            )
                        except mysql.connector.Error as err3:
                            # Method 4: Try with 127.0.0.1 and no password
                            conn = mysql.connector.connect(
                                host="127.0.0.1",
                                username="root",
                                database="Mydb"
                            )
                
                my_cursor = conn.cursor()
                sql = "delete from hospital where nameoftablet=%s"
                val = (self.Nameoftable.get(),)
                my_cursor.execute(sql,val)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Record has been deleted")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error connecting to MySQL: {err}")
                print(f"Detailed error: {err}")
    
    def fetch_data(self):
        try:
            # Try different connection methods
            try:
                # Method 1: Standard connection
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Test@1234",
                    database="Mydb"
                )
            except mysql.connector.Error as err:
                # Method 2: Try without password
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        database="Mydb"
                    )
                except mysql.connector.Error as err2:
                    # Method 3: Try with 127.0.0.1 instead of localhost
                    try:
                        conn = mysql.connector.connect(
                            host="127.0.0.1",
                            username="root",
                            password="Test@1234",
                            database="Mydb"
                        )
                    except mysql.connector.Error as err3:
                        # Method 4: Try with 127.0.0.1 and no password
                        conn = mysql.connector.connect(
                            host="127.0.0.1",
                            username="root",
                            database="Mydb"
                        )
            
            my_cursor = conn.cursor()
            my_cursor.execute("select * from hospital")
            rows = my_cursor.fetchall()
            if len(rows)!=0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for row in rows:
                    self.hospital_table.insert("",END,values=row)
                conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error connecting to MySQL: {err}")
            print(f"Detailed error: {err}")
    
    def get_cursor(self,event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content['values']
        
        self.Nameoftable.set(row[0])
        self.refrenceno.set(row[1])
        self.patientname.set(row[2])
        self.address.set(row[3])
        self.patientid.set(row[4])
        self.doctorname.set(row[5])
        self.lotno.set(row[6])
        self.issuedate.set(row[7])
        self.expdate.set(row[8])
        self.dailydose.set(row[9])
        self.sideeffect.set(row[10])
        self.bloodpressure.set(row[11])
        self.bloodsugar.set(row[12])
        self.storageadvice.set(row[13])                
    
    def iprecription(self):
        self.txtPrescription.delete("1.0",END)
        self.txtPrescription.insert(END,"Name of Tablet: \t\t"+self.Nameoftable.get()+"\n")
        self.txtPrescription.insert(END,"Refrence No.: \t\t"+self.refrenceno.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name: \t\t"+self.patientname.get()+"\n")
        self.txtPrescription.insert(END,"Address: \t\t"+self.address.get()+"\n")
        self.txtPrescription.insert(END,"Patient ID: \t\t"+self.patientid.get()+"\n")
        self.txtPrescription.insert(END,"Doctor Name: \t\t"+self.doctorname.get()+"\n")
        self.txtPrescription.insert(END,"Lot No.: \t\t"+self.lotno.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date: \t\t"+self.issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date: \t\t"+self.expdate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose: \t\t"+self.dailydose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect: \t\t"+self.sideeffect.get()+"\n")
        self.txtPrescription.insert(END,"Blood Pressure: \t\t"+self.bloodpressure.get()+"\n")
        self.txtPrescription.insert(END,"Blood Sugar: \t\t"+self.bloodsugar.get()+"\n")
        self.txtPrescription.insert(END,"Storage Advice: \t\t"+self.storageadvice.get()+"\n")
        self.txtPrescription.insert(END,"====================================\n")
        
        
        
root = Tk()
ob = Hospital(root)
root.mainloop()        