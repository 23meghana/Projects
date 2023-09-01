from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
 #set geometry for visible window
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition system")


        self.var_attend_ID = StringVar()
        self.var_attend_Roll = StringVar()
        self.var_attend_Name = StringVar()
        self.var_attend_Dep = StringVar()
        self.var_attend_Time = StringVar()
        self.var_attend_Date = StringVar()
        self.var_attend_Status = StringVar()
        
        





 #putting 3 Images
#first image
        img = Image.open(r"C:\Users\USER\Desktop\Face_Recognition System\college_images\Dpcoe.jpg")
        img = img.resize((350, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
# creating Label
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=400, height=130)

#second image
        img1 = Image.open(r"C:\Users\USER\Desktop\Face_Recognition System\college_images\face Recognition.png")
        img1 = img1.resize((350, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
# creating Label
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=400, y=0, width=400, height=130)

#third image
        img2 = Image.open(r"C:\Users\USER\Desktop\Face_Recognition System\college_images\collegeLogo.jpg")
        img2 = img2.resize((350, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
# creating Label
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800, y=0, width=400, height=130)

# background image
        img3 = Image.open(r"C:\Users\USER\Desktop\Face_Recognition System\college_images\background.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
# creating Label
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)


#main_label
        title_lbl=Label(bg_img,text="ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=50)

#ceating Frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=60,width=1515,height=590)

#left frame
        Left_Frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_Frame.place(x=10,y=10,width=600,height=570)

#studnt_info
        Studinfo_Frame = LabelFrame(Left_Frame, bd=2, relief=RIDGE, text="Student Info",font=("times new roman", 12, "bold"))
        Studinfo_Frame.place(x=5, y=30, width=590, height=305)
#STUDENT ID LABEL
        studID_label = Label(Studinfo_Frame, text="Student ID : ", font=("times new roman", 12, "bold"))
        studID_label.grid(row=0, column=0)

        StudentID_entry=ttk.Entry(Studinfo_Frame,width=20,textvariable=self.var_attend_ID,font=("times new roman", 12, "bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,sticky=W)
#STUDENT NAME LABEL
        studNAME_label = Label(Studinfo_Frame, text="Roll No : ", font=("times new roman", 12, "bold"))
        studNAME_label.grid(row=0, column=2)

        StudentNAME_entry = ttk.Entry(Studinfo_Frame, width=20,textvariable=self.var_attend_Roll, font=("times new roman", 12, "bold"))
        StudentNAME_entry.grid(row=0, column=3, padx=10,pady=5, sticky=W)
# STUDENT DIVISION LABEL
        studDiv_label = Label(Studinfo_Frame, text="Name : ", font=("times new roman", 12, "bold"))
        studDiv_label.grid(row=1, column=0)

        StudentDiv_entry = ttk.Entry(Studinfo_Frame, width=20,textvariable=self.var_attend_Name, font=("times new roman", 12, "bold"))
        StudentDiv_entry.grid(row=1, column=1, padx=10,pady=5, sticky=W)
# STUDENT RollNo LABEL
        studRollNo_label = Label(Studinfo_Frame, text="Department : ", font=("times new roman", 12, "bold"))
        studRollNo_label.grid(row=1, column=2)

        StudentRollNo_entry = ttk.Entry(Studinfo_Frame, width=20,textvariable=self.var_attend_Dep, font=("times new roman", 12, "bold"))
        StudentRollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
 # STUDENT Gender LABEL
        studGender_label = Label(Studinfo_Frame, text="Time : ", font=("times new roman", 12, "bold"))
        studGender_label.grid(row=2, column=0)

        StudentGender_entry = ttk.Entry(Studinfo_Frame, width=20,textvariable=self.var_attend_Time, font=("times new roman", 12, "bold"))
        StudentGender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
# STUDENT DOB LABEL
        studDOB_label = Label(Studinfo_Frame, text="Date : ", font=("times new roman", 12, "bold"))
        studDOB_label.grid(row=2, column=2)

        StudentDOB_entry = ttk.Entry(Studinfo_Frame, width=20,textvariable=self.var_attend_Date, font=("times new roman", 12, "bold"))
        StudentDOB_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
# STUDENT Email LABEL
        studEmail_label = Label(Studinfo_Frame, text="Status : ", font=("times new roman", 12, "bold"))
        studEmail_label.grid(row=3, column=0)

        #Search by Combo box
        Search_combo=ttk.Combobox(Studinfo_Frame,font=("times new roman",12,"bold"),width=18,textvariable=self.var_attend_Status,state="readonly")
        Search_combo["values"]=("--Select--","Present","Absent")
        Search_combo.current(0)
        Search_combo.grid(row=3,column=1,padx=2,pady=10)

 
# left Button frame
        button_Frame = LabelFrame(Studinfo_Frame, bd=2, relief=RIDGE)
        button_Frame.place(x=3, y=193, width=640, height=30)
#save button
        savebt = Button(button_Frame, text="Import CSV",command=self.importCsv, width=15, font=("times new roman", 12, "bold"), bg="gray")
        savebt.grid(row=0, column=0)
#update button
        updatebt=Button(button_Frame,text="Export CSV",command=self.exportCsv, width=15,font=("times new roman", 12, "bold"),bg="gray")
        updatebt.grid(row=0,column=1)
#delete  button
        deletebt = Button(button_Frame, text="Update", width=15, font=("times new roman", 12, "bold"), bg="gray")
        deletebt.grid(row=0, column=2)
# reset button
        resetbt = Button(button_Frame, text="Reset",command=self.reset_data, width=15, font=("times new roman", 12, "bold"), bg="gray")
        resetbt.grid(row=0, column=3)



#===============================right frame ================================================================================

#Right frame
        Right_Frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Marked Attendence",font=("times new roman",12,"bold"))
        Right_Frame.place(x=620,y=10,width=620,height=570)




#Right table Frame=========================================================================
        table_Frame = Frame(Right_Frame, bd=2, relief=RIDGE)
        table_Frame.place(x=5, y=40, width=600, height=500)
#scroll bar
        scroll_x = ttk.Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_Frame,orient=VERTICAL)
        self.AttendenceReportTable=ttk.Treeview(table_Frame,column=("Student_ID", "Roll No", "Name", "Department", "Time", "Date" ,"Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("Student_ID", text="Sudent_ID")
        self.AttendenceReportTable.heading("Roll No", text="Roll No")
        self.AttendenceReportTable.heading("Name", text="Name")
        self.AttendenceReportTable.heading("Department", text="Department")
        self.AttendenceReportTable.heading("Time", text="Time")
        self.AttendenceReportTable.heading("Date", text="Date")
        self.AttendenceReportTable.heading("Status", text="Status")

        self.AttendenceReportTable["show"]="headings"

#set column width
        self.AttendenceReportTable.column("Student_ID", width=80)
        self.AttendenceReportTable.column("Roll No", width=80)
        self.AttendenceReportTable.column("Name", width=80)
        self.AttendenceReportTable.column("Department", width=80)
        self.AttendenceReportTable.column("Time", width=80)
        self.AttendenceReportTable.column("Date", width=80)
        self.AttendenceReportTable.column("Status", width=80)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)



#=============================fetch data============================
    def fetchData(self, rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)


#=============================Import CSV============================


    def importCsv(self):   
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

#=============================Export CSV============================

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimeter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data Exported to "+os.path.basename(fln)+"sucessflly exported")
        except Exception as es:
                messagebox.showerror("error",f"Due To:{str(es)}",parent=self.root)

#============================Get cursor=========================

    def get_cursor(self,event=""):
        cursor_focus=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_focus)
        data=content["values"]

        self.var_attend_ID.set(data[0]),
        self.var_attend_Roll.set(data[1]),
        self.var_attend_Name.set(data[2]),
        self.var_attend_Dep.set(data[3]),
        self.var_attend_Time.set(data[4]),
        self.var_attend_Date.set(data[5]),
        self.var_attend_Status.set(data[6])


#=================reset button ========================

    def reset_data(self):
        self.var_attend_ID.set(""),
        self.var_attend_Roll.set(""),
        self.var_attend_Name.set(""),
        self.var_attend_Dep.set(""),
        self.var_attend_Time.set(""),
        self.var_attend_Date.set(""),
        self.var_attend_Status.set("")















if __name__ =="__main__":
    root=Tk()
    obj= Attendence(root)
    root.mainloop()
