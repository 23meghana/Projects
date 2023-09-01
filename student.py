from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
#from mysql.connector import MySQLConnection, CMySQLConnection
#from time import sleep
#from mysql.connector.pooling import PooledMySQLConnection
import os


class Student:
    def __init__(self,root):
        self.root=root
 #set geometry for visible window
        self.root.geometry("1530x790+0+0")
        self.root.title("Student")

    #=====================variables==================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()






 #putting 3 Images
#first image
        img = Image.open(r"C:\Users\USER\Desktop\Face_Recognition System\college_images\Dpcoe.jpg")
        img = img.resize((350, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
# creating Label
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=400, height=130)

#second image
        img1 = Image.open(r"C:\Users\USER\Desktop\Face_Recognition System\college_images\studentgroup.jpg")
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
        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1380,height=53)

#ceating Frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=60,width=1515,height=590)

#left frame
        Left_Frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Students Entry",font=("times new roman",12,"bold"))
        Left_Frame.place(x=10,y=10,width=600,height=450)
#course_info
        course_Frame = LabelFrame(Left_Frame, bd=2, relief=RIDGE, text="Department/Course/Year/Semester",font=("times new roman", 12, "bold"))
        course_Frame.place(x=5, y=8, width=590, height=120)

        dept_label=Label(course_Frame,text="Department",font=("times new roman",12,"bold"))
        dept_label.grid(row=0,column=0)
    #combo box1
        dept_combo=ttk.Combobox(course_Frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dept_combo["values"]=("--None--","E&TC","Computer","IT","Mechanical","Civil")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10)

        dept_label = Label(course_Frame, text="Course", font=("times new roman", 12, "bold"))
        dept_label.grid(row=0, column=2)
    # combo box2
        dept_combo = ttk.Combobox(course_Frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), width=17, state="readonly")
        dept_combo["values"] = ("--None--","FE", "SE","TE", "BE")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=3, padx=2, pady=10)

        dept_label = Label(course_Frame, text="Year", font=("times new roman", 12, "bold"))
        dept_label.grid(row=1, column=0)
    # combo box3
        dept_combo = ttk.Combobox(course_Frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), width=17, state="readonly")
        dept_combo["values"] = ("--None--","2020-21","2021-22","2022-23","2023-24")
        dept_combo.current(0)
        dept_combo.grid(row=1, column=1, padx=2, pady=10)

        dept_label = Label(course_Frame, text="Semester", font=("times new roman", 12, "bold"))
        dept_label.grid(row=1, column=2)
    # combo box4
        dept_combo = ttk.Combobox(course_Frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=17, state="readonly")
        dept_combo["values"] = ("--None-- ","First", "Second", "Third", "Forth", "Fifth", "Sixth","Seventh","Eighth")
        dept_combo.current(0)
        dept_combo.grid(row=1, column=3, padx=2, pady=10)

#studnt_info
        Studinfo_Frame = LabelFrame(Left_Frame, bd=2, relief=RIDGE, text="Student Info",font=("times new roman", 12, "bold"))
        Studinfo_Frame.place(x=5, y=130, width=590, height=305)
#STUDENT ID LABEL
        studID_label = Label(Studinfo_Frame, text="Student ID : ", font=("times new roman", 12, "bold"))
        studID_label.grid(row=0, column=0)

        StudentID_entry=ttk.Entry(Studinfo_Frame,textvariable=self.var_std_id,width=20,font=("times new roman", 12, "bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,sticky=W)
#STUDENT NAME LABEL
        studNAME_label = Label(Studinfo_Frame, text="Student Name : ", font=("times new roman", 12, "bold"))
        studNAME_label.grid(row=0, column=2)

        StudentNAME_entry = ttk.Entry(Studinfo_Frame,textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        StudentNAME_entry.grid(row=0, column=3, padx=10,pady=5, sticky=W)
# STUDENT DIVISION LABEL
        studDiv_label = Label(Studinfo_Frame, text="Division : ", font=("times new roman", 12, "bold"))
        studDiv_label.grid(row=1, column=0)

        StudentDiv_entry = ttk.Entry(Studinfo_Frame,textvariable=self.var_div, width=20, font=("times new roman", 12, "bold"))
        StudentDiv_entry.grid(row=1, column=1, padx=10,pady=5, sticky=W)
# STUDENT RollNo LABEL
        studRollNo_label = Label(Studinfo_Frame, text="Roll NO. : ", font=("times new roman", 12, "bold"))
        studRollNo_label.grid(row=1, column=2)

        StudentRollNo_entry = ttk.Entry(Studinfo_Frame,textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        StudentRollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
 # STUDENT Gender LABEL
        studGender_label = Label(Studinfo_Frame, text="Gender : ", font=("times new roman", 12, "bold"))
        studGender_label.grid(row=2, column=0)

        StudentGender_entry = ttk.Entry(Studinfo_Frame,textvariable=self.var_gender, width=20, font=("times new roman", 12, "bold"))
        StudentGender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
# STUDENT DOB LABEL
        studDOB_label = Label(Studinfo_Frame, text="DOB : ", font=("times new roman", 12, "bold"))
        studDOB_label.grid(row=2, column=2)

        StudentDOB_entry = ttk.Entry(Studinfo_Frame,textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        StudentDOB_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
# STUDENT Email LABEL
        studEmail_label = Label(Studinfo_Frame, text="Email ID : ", font=("times new roman", 12, "bold"))
        studEmail_label.grid(row=3, column=0)

        StudentEmail_entry = ttk.Entry(Studinfo_Frame,textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        StudentEmail_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
# STUDENT PhoneNO. LABEL
        studPhone_label = Label(Studinfo_Frame, text="Phone NO. : ", font=("times new roman", 12, "bold"))
        studPhone_label.grid(row=3, column=2)

        StudentPhone_entry = ttk.Entry(Studinfo_Frame,textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        StudentPhone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
# STUDENT Address LABEL
        studAddress_label = Label(Studinfo_Frame, text="Address : ", font=("times new roman", 12, "bold"))
        studAddress_label.grid(row=4, column=0)

        StudentAddress_entry = ttk.Entry(Studinfo_Frame,textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        StudentAddress_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
#radio button

        self.var_radio1=StringVar()
        radiobtn=ttk.Radiobutton(Studinfo_Frame,variable=self.var_radio1,text="Take Photo ",value="Yes")
        radiobtn.grid(row=5,column=1)
# left Button frame
        button_Frame = LabelFrame(Studinfo_Frame, bd=2, relief=RIDGE)
        button_Frame.place(x=5, y=193, width=650, height=30)
#save button
        savebt = Button(button_Frame, text="Save",command=self.add_data, width=15, font=("times new roman", 12, "bold"), bg="gray")
        savebt.grid(row=0, column=0)
#update button
        updatebt=Button(button_Frame,text="Update", command=self.update_data, width=15,font=("times new roman", 12, "bold"),bg="gray")
        updatebt.grid(row=0,column=1)
#delete  button
        deletebt = Button(button_Frame, text="Delete", command=self.delete_data, width=15, font=("times new roman", 12, "bold"), bg="gray")
        deletebt.grid(row=0, column=2)
# reset button
        resetbt = Button(button_Frame, text="Reset",command=self.reset_data,  width=15, font=("times new roman", 12, "bold"), bg="gray")
        resetbt.grid(row=0, column=3)

# left Button frame
        button2_Frame = LabelFrame(Studinfo_Frame, bd=2, relief=RIDGE)
        button2_Frame.place(x=5, y=230, width=580, height=30)
# take face sample button
        TakeFacebt = Button(button2_Frame,command=self.generate_dataset,  text="Take Face Sample", width=30, font=("times new roman", 12, "bold"), bg="gray")
        TakeFacebt.grid(row=0, column=0)
# reset button
        updatefacebt = Button(button2_Frame, text="Update Face Sample", width=32, font=("times new roman", 12, "bold"), bg="gray")
        updatefacebt.grid(row=0, column=1)



#Right frame
        Right_Frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_Frame.place(x=620,y=10,width=620,height=450)

# Search Frame
        search_Frame = LabelFrame(Right_Frame, bd=2, relief=RIDGE, text="Search Systems",font=("times new roman", 12, "bold"))
        search_Frame.place(x=5, y=20, width=610, height=70)

        search_label = Label(search_Frame, text="Search By : ", font=("times new roman", 12, "bold"))
        search_label.grid(row=0, column=0,padx=10,pady=5,sticky=W)

#Search by Combo box
        Search_combo=ttk.Combobox(search_Frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        Search_combo["values"]=("--Select--","Roll No.","PhoneNo")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10)
# search entry
        search_entry = ttk.Entry(search_Frame, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

# search button
        search_bt = Button(search_Frame, text="Search", width=8, font=("times new roman", 12, "bold"),bg="gray")
        search_bt.grid(row=0, column=3,padx=4)
# show allbutton
        showall_bt = Button(search_Frame, text="Search All", width=8, font=("times new roman", 12, "bold"),bg="gray")
        showall_bt.grid(row=0, column=4,padx=4)


#Right table Frame=========================================================================
        table_Frame = Frame(Right_Frame, bd=2, relief=RIDGE)
        table_Frame.place(x=5, y=100, width=610, height=305)
#scroll bar
        scroll_x = ttk.Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_Frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_Frame,column=("Department", "Course", "Year", "Sem", "ID", "Name" ,"Div", "RollNo", "Gender", "DOB", "Email", "Phone", "Address", "Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.xview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("ID", text="StudentId")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("RollNo", text="RollNo")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Div", text="Division")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"


#set column width
        self.student_table.column("Department", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("RollNo", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Div", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Photo", width=150)
        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



#==================Function for addinfo data=================

    def add_data(self):
        if self.var_dep.get()=="__None__" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields Required",parent=self.root)
        else:
            try:

                conn = mysql.connector.connect(host="localhost", user="root", password="Crypto@rt99",database="face_recognizer",auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_radio1.get()
                        ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess", "Added Sucessfully!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error","Duplicate entry not allowed",parent=self.root)

#==============Fetch Data=============

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Crypto@rt99", database="face_recognizer",auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        #fetch all data to data
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#=========update function===============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_radio1.set(data[13])

#===============update button connection==========
    def update_data(self):

        if self.var_dep.get()=="__None__" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields Required",parent=self.root)
        else:
            
            try:
                Update=messagebox.askyesno("Update","do you wnat to update these details",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Crypto@rt99", database="face_recognizer",auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(

                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Sucess","Data Updated!!!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("error",f"Due To:{str(es)}",parent=self.root)


#==========================delete button function=========================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("error", "Student Id Required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("DELETE DETAILS?", "want to delete", parent=self.root)
                if delete>0:
                    conn= mysql.connector.connect(host="localhost", user="root", password="Crypto@rt99",database="face_recognizer" ,auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Success", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"due to:{str(es)}", parent=self.root)

#====================Reset Button=
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set(" ")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")


#===================Take photo sample===================

    def generate_dataset(self):
        if self.var_dep.get() == "__None__" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields Required", parent=self.root)
        else:
            try:
                #establish conncction
                conn=mysql.connector.connect(host="localhost", user="root", password="Crypto@rt99",database="face_recognizer",auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1

                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
#============Load predefined data on face frontal from opencv=============

                # load the classifier file
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Process Completed")
            except Exception as es:
                messagebox.showerror("Error", f"due to:{str(es)}", parent=self.root)









if __name__ =="__main__":
    root=Tk()
    obj= Student(root)
    root.mainloop()