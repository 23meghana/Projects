from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
import numpy as np
import cv2
from tkinter import messagebox
import mysql.connector












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

        #====================== Recognize Face=====================
        
def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Crypto@rt27", database="stud_data")
                my_cursor = conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(str(id) for id in n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)


                if confidence>77:
                    
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Deparment:{d}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
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

            if cv2.waitKey(1)& 0xFF == ord('q'):
                break
        video_cap.release()
        cv2.destroyAllWindows()
