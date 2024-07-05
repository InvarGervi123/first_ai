import cv2
import os

files = os.listdir('images')

for file in files:

    img = cv2.imread('images/'+file)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = cv2.CascadeClassifier('faces.xml')

    results = faces.detectMultiScale(gray,scaleFactor=1.8,minNeighbors=4)

    for (x,y,w,h) in results:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness=3)

    cv2.imshow('results',img)
    cv2.waitKey(0)

    cv2.addText("img",'AAAAA',pointSize=(3,4,5))