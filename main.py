import cv2
import os

#cap = cv2.VideoCapture("Tami_in_bus.mp4")

files = os.listdir('images')

for file in files:

    img = cv2.imread('images/'+file)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = cv2.CascadeClassifier('faces.xml')

    results = faces.detectMultiScale(gray,scaleFactor=1.8,minNeighbors=4)

    for (x,y,w,h) in results:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness=3)



        cv2.putText(img,"HOMO",(x+100,y-5),cv2.FONT_HERSHEY_PLAIN,8,(0,0,255),2)

       # new_img = cv2.resize(img, (1920, 1080))

    cv2.imshow('results',img)#new_img)
    cv2.waitKey(0)

