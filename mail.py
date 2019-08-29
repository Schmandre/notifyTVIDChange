import smtplib
import socket
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

senderEmail = "sender@domain.com"
empfangsEmail = "empfaenger@domain.com"
msg = MIMEMultipart()
msg['From'] = senderEmail
msg['To'] = empfangsEmail
msg['X-Priority'] = '2'
msg['Subject'] = "Deine TV ID hat sich geaendert"
hostname = socket.gethostname()
tvIDOld = open("shortIDOld.txt").readlines()
tvIDNew = open("shortID.txt").readlines()

emailText = "Die Teamviewer ID vom RAPI "+hostname+" hat sich von "+str(tvIDOld)+" auf "+str(tvIDNew)+" geaendert"
msg.attach(MIMEText(emailText, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587) #SMTP Server
server.starttls()
server.login(senderEmail, "Passwort") #Passwort der Sendeadresse
text = msg.as_string()
server.sendmail(senderEmail, empfangsEmail, text)
server.quit()
