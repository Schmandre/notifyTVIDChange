import smtplib
import socket
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#INIT
senderEmail = "sender@domain.com"
senderPassword = "PASSWORD"
empfangsEmail = "empfaenger@domain.com"
smtpServer = "CHANGEME"
smtpServerPort = 25
nameKunde = "CHANGEME"

#Get local IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip=s.getsockname()[0]
s.close()

msg = MIMEMultipart()
msg['From'] = senderEmail
msg['To'] = empfangsEmail
msg['X-Priority'] = '2'
msg['Subject'] = "Eine TeamViewer ID bei "+nameKunde+" hat sich geaendert"
hostname = socket.gethostname()
tvIDOld = open("shortIDOld.txt").readlines()
tvIDNew = open("shortID.txt").readlines()
mailUsername=open("login.txt").readlines()
mailPassword=open("login.txt").readlines()

emailText = "Kunde: "+nameKunde+" <br> Hostname: "+hostname+" <br> IP: "+str(ip)+" <br> TeamViewer ID alt: "+str(tvIDOld)+" <br> TeamViewer ID neu: "+str(tvIDNew)+""
msg.attach(MIMEText(emailText, 'html'))
server = smtplib.SMTP(smtpServer, smtpServerPort)
server.starttls()
server.login(senderEmail, senderPassword)
text = msg.as_string()
server.sendmail(senderEmail, empfangsEmail, text)
server.quit()