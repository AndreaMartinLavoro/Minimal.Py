import cv2
from cv2 import cv2
import tkinter as tk
import requests

#----------------------------------------------------------------
window = tk.Tk()			    #creo la finestra(widget)
window.geometry("900x500")
window.title("FACE RECON")
window.grid_columnconfigure(0, weight=1)
#----------------------------------------------------------------
def facerecon():
    textwidget.delete("1.0","end")
    num = 0
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(text_input.get(), 1 )
    if img == None: # older numpy / py2
     textwidget.insert(tk.INSERT, ("Errore"))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if gray == None: # older numpy / py2
     textwidget.insert(tk.INSERT, ("Errore2"))
    faces = face_cascade.detectMultiScale(gray, 1.2, 4) #1.2 scale
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        num=num+1
    textwidget.insert(tk.INSERT, ("Entita' riconosciute :",num))
    textwidget.insert(tk.INSERT, cv2.imshow('img', img))
    cv2.waitKey()
#----------------------------------------------------------------
text_input = tk.Entry()                                 #input text
text_input.grid(row=1, column=0,sticky="WE", pady=10, padx=10)
#----------------------------------------------------------------
send_button = tk.Button(text="START", command=facerecon)
send_button.grid(row=2, column=0, sticky="WE", pady=10 ,padx=10)
#----------------------------------------------------------------
#blocco di testo
textwidget = tk.Text()
textwidget.insert(tk.END, "Entita' riconosciute :")
textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)
#----------------------------------------------------------------
if __name__=="__main__":
    window.mainloop()
