import smtplib
import socket
import config
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#Get local IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip=s.getsockname()[0]
s.close()

#DoNotEdit
msg = MIMEMultipart()
msg['From'] = config.senderEmail
msg['To'] = config.receiverEmail
msg['X-Priority'] = '2'
msg['Subject'] = "TeamViewer ID at "+config.nameCustomer+" has changed"
hostname = socket.gethostname()
IDShortOld = file(config.pathToScripts+'shortIDOld.txt', 'r')
outputShortIDOld = IDShortOld.readlines()[0]
IDShortOld.close()
IDShortNew = file(config.pathToScripts+'shortID.txt', 'r')
outputShortID = IDShortNew.readlines()[0]
IDShortNew.close()

emailText = "<hr><table><tr><td>Customer:</td><td>"+config.nameCustomer+"</td></tr><tr><td>Hostname:</td><td>"+hostname+"</td></tr><tr><td>IP:</td><td>"+str(ip)+"</td></tr><tr><td>TeamViewer ID old:</td><td>"+str(outputShortIDOld)+"</td></tr><tr><td>TeamViewer ID new:</td><td>"+str(outputShortID)+"</td></tr></table><hr>"

msg.attach(MIMEText(emailText, 'html'))
server = smtplib.SMTP(config.smtpServer, config.smtpServerPort)
server.starttls()
server.login(config.username, config.password)
text = msg.as_string()
server.sendmail(config.senderEmail, config.receiverEmail, text)
server.quit()
