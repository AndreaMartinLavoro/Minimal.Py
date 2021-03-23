import math
import os
import time

decibel = math.log10 (17.0)
angolo = 1.5
altezza = math.sin(angolo)

#---------------------------------------------------------------
#definizione di una funzione
def UnaRigaVuota():
  print ()
#---------------------------------------------------------------
#definizione di una funzione con parametri
def Stampa2Volte(Valore):
  print (Valore, Valore)
Stampa2Volte('Pippo'*4)
x = 5
#questo è un if
if x > 0:
  print ("x e' positivo")
#pass serve per non fare nulla
if x < 0:
  pass
#---------------------------------------------------------------
#esempio complesso
def StampaParita(x):
  if x%2 == 0:
    print (x, "e' pari")
  else:
    print (x, "e' dispari")
print (StampaParita(7))
#---------------------------------------------------------------
#ricorsione
def ContoAllaRovescia(n):
  if n == 0:
    print ("Partenza!")
  else:
    print (n)
    ContoAllaRovescia(n-1)
ContoAllaRovescia(10)
#Input da tastiera per Interi
Inserimento = input ("Inserisci un numero : ")
print (Inserimento)
#Input da tastiera
#raw_input ?
Inserimento = input ("Qual e' il tuo nome? ")
print (Inserimento)
#---------------------------------------------------------------
#funzione return blocca il programma
def StampaLogaritmo(x):
  if x <= 0:
    print ("Inserire solo numeri positivi!")
    return
#non viene eseguito
  risultato = math.log(x)
  print ("Il logaritmo di",x,"e'", risultato)
print (StampaLogaritmo(0))
#---------------------------------------------------------------
def AreaDelCerchio(Raggio):                 #Area Del Cerchio
  print ("L'Area del cerchio vale:")
  return math.pi * Raggio**2
#---------------------------------------------------------------
def ValoreAssoluto(x):                      #Valore Assoluto
  if x < 0:
    print ("Il valore assoluto vale :")
    return -x
  elif x > 0:
    print ("Il valore assoluto vale :")
    return x
#---------------------------------------------------------------
def DistanzaTraDuePunti(x1, y1, x2, y2):    #Distanza tra due punti
  dx = x2 - x1
  dy = y2 - y1
  DistQuadrata = dx**2 + dy**2
  Risultato = math.sqrt(DistQuadrata)
  print ("La distanza tra i due punti e' di :")
  return Risultato
#---------------------------------------------------------------
def Divisibile(x, y):                       #Divisibile
  print ("E' ",x%y == 0," che x e y sono divisibili")
  return 
#---------------------------------------------------------------
def Fattoriale(n):                          #Fattoriale
  if n == 0:
    print ("Il fattoriale di n vale :")
    return 1
  else:
    FattorialeMenoUno = Fattoriale(n-1)
    Risultato = n * FattorialeMenoUno
    print ("Il fattoriale di n vale :")
    return Risultato
#---------------------------------------------------------------
def ContoAllaRovescia(n):                   #Conto alla rovesia
  while n > 0:
    print (n)
    n = n-1
    time.sleep(1)                           #delay
  return "Partenza!"
#---------------------------------------------------------------
def Tabella():                   #tabella
  x = 1.0
  while x < 100.0:
    print (x, '\t', math.log(x)/math.log(2.0))
    x = x * 2.0
  return ""
#---------------------------------------------------------------
def Stringhe(Frutto):                   #Stringhe
  Indice = 0
  while Indice < len(Frutto):
    Lettera = Frutto[Indice]
    print (Lettera)
    Indice = Indice + 1
  return ""
#---------------------------------------------------------------
def StringheNomi():                   #Stringhe con for
  Prefissi = "JKLMNOPQ"
  Suffisso = "ack"

  for Lettera in Prefissi:
    print (Lettera + Suffisso)
#---------------------------------------------------------------
def Porz():                   #PORZIONI (SUBSTRING)
  s = "Pietro, Paolo e Maria"
  print (s[0:6])
  print (s[8:13])
  print (s[16:21])
  return ""
#---------------------------------------------------------------
def Mut(x):                   #Muta stringhe
  Saluto = x
  NuovoSaluto = 'M' + Saluto[1:]
  print (NuovoSaluto)
  return ""
#---------------------------------------------------------------
def Trova(Stringa, Carattere):
  Indice = 0
  while Indice < len(Stringa):
    if Stringa[Indice] == Carattere:
      return Indice
    Indice = Indice + 1
  return -1
#---------------------------------------------------------------
def List(x,y,z):
  Squadre = [x,y,z]

  i = 0
  while i < len(Squadre):
    print (Squadre[i])
    i = i + 1
  return ""
#---------------------------------------------------------------
def Id():
  a = "banana"
  b = "banana"
  return (id(a),id(b))
#---------------------------------------------------------------
def Mat():
  Matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  print ("Matrice[1]",Matrice[1])
  print ("Matrice[1][1]",Matrice[1][1])
#---------------------------------------------------------------
def Tup():
  tupla = ('a', 'b', 'c', 'd', 'e')
  t1=('a',)
  print ("tupla[0]",tupla[0])
  print ("type(tupla)",type(tupla))
  print ("type(t1)",type(t1))
#---------------------------------------------------------------
import random
def R():
  for i in range(10):
    x = random.random()
    print (x)
#---------------------------------------------------------------
def CopiaFile(Originale, Copia):
  f1 = open(Originale, "r") #al posto del Originale puoi inserire il path della directori
  f2 = open(Copia, "w")
  while 1:
    Testo = f1.read(50)
    if Testo == "":
      break
    f2.write(Testo)
  f1.close()
  f2.close()
  return
#---------------------------------------------------------------
def Menu():
  print ("Menu")
  print ("1 - Area del Cerchio")
  print ("2 - Distanza tra due Punti")
  print ("3 - E' divisibile ?")
  print ("4 - Fattoriale")
  print ("5 - Contatore")
  print ("6 - Tabella")
  print ("7 - Stringhe")
  print ("8 - Stringhe Nomi")
  print ("9 - Porzioni di Stringa")
  print ("10 - Muta string")
  print ("11 - Trova un carattere")
  print ("12 - Lista")
  print ("13 - ID")
  print ("14 - Metrice")
  print ("15 - tupla")
  print ("16 - random")
  print ("17 - Copia di file")
  s = input (":")
  if s == "1":
    print (AreaDelCerchio(int(input ("raggio:"))))
  if s == "2":
    print (DistanzaTraDuePunti(int(input ("x1:")),int(input ("x2:")),int(input ("y1:")),int(input ("y2:"))))
  if s == "3":
    Divisibile(int(input ("x:")), int(input ("y:")))
  if s == "4":
    print (Fattoriale(int(input ("n:"))))
  if s == "5":
    print (ContoAllaRovescia(int(input ("Da che numero vuoi partire ?"))))
  if s == "6":
    print (Tabella())
  if s == "7":
    print (Stringhe(input ("Inserisci una Stringa :")))
  if s == "8":
    print (StringheNomi())
  if s == "9":
    print (Porz())
  if s == "10":
    print (Mut(input ("Inserisci una Stringa :")))
  if s == "11":
    string=input ("Inserisci una Stringa :")
    carattere=input ("Inserisci un Carattere :")
    if Trova(string,carattere)!=-1:
      print ("Il carattere si trova in posizione",Trova(string,carattere))
    else:
      print ("Il carattere non è presente nella stringa")
  if s == "12":
    print (List(input ("Inserisci una Stringa :"),input ("Inserisci una Stringa :"),input ("Inserisci una Stringa :")))
  if s == "13":
    print (Id())
  if s == "14":
    Mat()
  if s == "15":
    Tup()
  if s == "16":
    R()
  if s == "17":
    CopiaFile(input ("Inserisci il file di Input :"),input ("Inserisci il file di Output :"))
  else:
    Menu()
