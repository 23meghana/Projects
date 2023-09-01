from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime
import numpy as np
import cv2
from tkinter import messagebox
import mysql.connector
from attendence import Attendence

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
 #set geometry for visible window
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition system")

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
        title_lbl=Label(bg_img,text="FACE RECOGNTION ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=50)

#student_button
        img4 = Image.open(r"C:\Users\USER\Desktop\Face_Recognition System\college_images\Student.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
#convert_img_to_button
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=220,height=160)

        b1_1= Button(bg_img,text="Student Details",command=self.student_details, cursor="hand2")
        b1_1.place(x=100, y=260, width=220, height=30)

#Detect Face button
        img5 = Image.open(r"C:\Users\USER\Desktop\Face_Recognition System\college_images\Facerecognize.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        # convert_img_to_button
        b1 = Button(bg_img, image=self.photoimg5, command=self.face_recog, cursor="hand2")
        b1.place(x=370, y=100, width=220, height=160)

        b1_1 = Button(bg_img, text="Face Detector", command=self.face_recog, cursor="hand2")
        b1_1.place(x=370, y=260, width=220, height=30)

#Atendence Face button
        img6 = Image.open(r"C:\Users\USER\Desktop\Face_Recognition System\college_images\Attendence.png")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        # convert_img_to_button
        b1 = Button(bg_img, image=self.photoimg6,command=self.attendence_data, cursor="hand2")
        b1.place(x=640, y=100, width=220, height=160)

        b1_1 = Button(bg_img, text="Attendence",command=self.attendence_data, cursor="hand2")
        b1_1.place(x=640, y=260, width=220, height=30)

#Help button
        img7 = Image.open(r"C:\Users\USER\Desktop\Face_Recognition System\college_images\HelpDesk.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        # convert_img_to_button
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=910, y=100, width=220, height=160)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2")
        b1_1.place(x=910, y=260, width=220, height=30)

#Train Face button
        img8 = Image.open(r"C:\Users\USER\Desktop\Face_Recognition System\college_images\TrainFace.png")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        # convert_img_to_button
        b1 = Button(bg_img, image=self.photoimg8, command=self.train_classifier, cursor="hand2")
        b1.place(x=370, y=320, width=220, height=160)

        b1_1 = Button(bg_img, text="Train Images", command=self.train_classifier, cursor="hand2")
        b1_1.place(x=370, y=478, width=220, height=30)

#Photos button
        img9 = Image.open(r"C:\Users\USER\Desktop\Face_Recognition System\college_images\Photos.png")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        # convert_img_to_button
        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=640, y=320, width=220, height=160)

        b1_1 = Button(bg_img, text="Data", cursor="hand2",command=self.open_img)
        b1_1.place(x=640, y=478, width=220, height=30)

#==========================open photos folder============#
    def open_img(self):
        os.startfile("data")
        
#===========================Connecting pages buton+===========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        facess=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #convert to gray scale
            imageNp=np.array(img,'uint8')       # uint8 is a  datatype
            id=int(os.path.split(image)[1].split('.')[1])

            facess.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #======================train classifier and save=============
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(facess,ids)
        recognizer.write("classfier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Dataset Training Completed!!")

#=============================mark Attendence=======================================================================================
    def mark_attendence(self,i,r,n,d):
        with open("attendence.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                 now=datetime.now()
                 d1=now.strftime("%d/%m/%y")
                 dtString=now.strftime("%H/%M/%S")
                 f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
            






        #====================== Recognize Face=====================
        
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

            coord=[]
 
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Crypto@rt99", database="face_recognizer")
                my_cursor = conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)


                if confidence>77:
                    
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Deparment:{d}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord= draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classfier.xml")

        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Recogniting Faces...",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()    






























if __name__ =="__main__":
    root=Tk()
    obj= Face_Recognition_System(root)
    root.mainloop()
