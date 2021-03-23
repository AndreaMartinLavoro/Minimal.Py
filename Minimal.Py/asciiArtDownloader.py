import tkinter as tk
import requests
#----------------------------------------------------------------
window = tk.Tk()			    #creo la finestra(widget)
window.geometry("900x500")
window.title("ASCII ART DOWNLOADER")
window.grid_columnconfigure(0, weight=1)
#----------------------------------------------------------------
def download_ascii():
    if text_input.get():
#conversione in ascci art----------------------------------------
        user_input = text_input.get()
        payload = {"text": user_input}
        response = requests.get("http://artii.herokuapp.com/make",
                                params=payload)
#----------------------------------------------------------------
        text_response = response.text
    else:text_response = "Aggiungi una parola o una frase nel campo input!"
    #blocco di testo
    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)
#----------------------------------------------------------------
    #pedipagina
    credit_label = tk.Label(window, text="ascii art by artii.herokuapp.com")
    credit_label.grid(row=4, column=0, sticky="S", pady=10)
    #appare dopo l'esecuzione del programma
#----------------------------------------------------------------
welcome_label = tk.Label(window, text="Welcome! Aggiungi una parola o una frase da scaricare:", font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)
#----------------------------------------------------------------
text_input = tk.Entry()                                 #input text
text_input.grid(row=1, column=0,sticky="WE", pady=10, padx=10)
#----------------------------------------------------------------
download_button = tk.Button(text="DOWNLOAD ASCII ART", command=download_ascii)
download_button.grid(row=2, column=0, sticky="WE", pady=10 ,padx=10)
#----------------------------------------------------------------
if __name__=="__main__":
    window.mainloop()
    
