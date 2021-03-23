import cv2 #pip install opencv-python
face_cascade = cv2.CascadeClassifier('lib/haarcascade_frontalface_default.xml')
img = cv2.imread(input("Inserisci il nome intero dell'immagine da esaminare :"))
num = 0
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    num=num+1
print ("Le persone nella foto sono ", num)
cv2.imshow('img', img)
cv2.waitKey()

