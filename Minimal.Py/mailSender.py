import smtplib
from email.message import EmailMessage

Sender_Email = "la_tua_email"
Reciever_Email = "la_mail_a_cui_vuoi_inoltrare_il_messaggio"
Password = "la_tua_password"
eSubject = "il_soggetto_della_mail"
eBody = "il_body_della_mail"
eSmtp = 'smtp.gmail.com'
ePort = 465

newMessage = EmailMessage()    
newMessage['Subject'] = eSubject 
newMessage['From'] = Sender_Email  
newMessage['To'] = Reciever_Email 
newMessage.set_content(eBody) 
with smtplib.SMTP_SSL(eSmtp, ePort) as smtp:
    
    smtp.login(Sender_Email, Password) 
    contatore = 0
    while contatore <= 10:
        smtp.send_message(newMessage)
        contatore = contatore + 1