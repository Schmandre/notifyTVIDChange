import smtplib
import socket
import config
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#INIT
senderEmail = "sender@domain.com"
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
IDShortOld = file('shortIDOld.txt', 'r')
lines = IDShortOld.readlines()
outputShortIDOld = lines[0]
IDShortOld.close()
IDShortNew = file('shortID.txt', 'r')
lines = IDShortNew.readlines()
OutputShortID = lines[0]
IDShortNew.close()

emailText = "Kunde: "+nameKunde+" <br> Hostname: "+hostname+" <br> IP: "+str(ip)+" <br> TeamViewer ID alt: "+str(outputShortIDOld)+" <br> TeamViewer ID neu: "+str(OutputShortID)+""

msg.attach(MIMEText(emailText, 'html'))
server = smtplib.SMTP(smtpServer, smtpServerPort)
server.starttls()
server.login(config.username, config.password)
text = msg.as_string()
server.sendmail(senderEmail, empfangsEmail, text)
server.quit()