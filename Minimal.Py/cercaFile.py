# py -m pip install --upgrade pip --user
import tkinter as tk
import requests #python -m pip install requests
#----------------------------------------------------------------
window = tk.Tk()			    #creo la finestra(widget)
window.geometry("900x500")
window.title("ASCII ART DOWNLOADER")
window.grid_columnconfigure(0, weight=1)
#----------------------------------------------------------------
def FileEsiste(event):
  textwidget = tk.Text()
  textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)
  try:
    f = open(text_input.get())
    f.close()
    textwidget.insert(tk.END, "File Trovato!")
  except:
    textwidget.insert(tk.END, "File Non Trovato!")
window.bind('<Return>', FileEsiste)
#----------------------------------------------------------------
welcome_label = tk.Label(window, text="Welcome! Aggiungi il nome intero del file da cercare :", font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)
#----------------------------------------------------------------
text_input = tk.Entry()                                 #input text
text_input.grid(row=1, column=0,sticky="WE", pady=10, padx=10)
#----------------------------------------------------------------
download_button = tk.Button(text="CERCA", command=FileEsiste)
download_button.grid(row=2, column=0, sticky="WE", pady=10 ,padx=10)
#----------------------------------------------------------------
#window.bind('<Return>', FileEsiste)
#----------------------------------------------------------------
if __name__=="__main__":
    window.mainloop()
