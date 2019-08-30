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

msg = MIMEMultipart()
msg['From'] = config.senderEmail
msg['To'] = config.receiverEmail
msg['X-Priority'] = '2'
msg['Subject'] = "TeamViewer ID at "+config.nameCustomer+" has changed"
hostname = socket.gethostname()
IDShortOld = file('shortIDOld.txt', 'r')
outputShortIDOld = IDShortOld.readlines()[0]
IDShortOld.close()
IDShortNew = file('shortID.txt', 'r')
outputShortID = IDShortNew.readlines()[0]
IDShortNew.close()

emailText = "Customer: "+config.nameCustomer+" <br> Hostname: "+hostname+" <br> IP: "+str(ip)+" <br> TeamViewer ID old: "+str(outputShortIDOld)+" <br> TeamViewer ID new: "+str(outputShortID)+""

msg.attach(MIMEText(emailText, 'html'))
server = smtplib.SMTP(config.smtpServer, config.smtpServerPort)
server.starttls()
server.login(config.username, config.password)
text = msg.as_string()
server.sendmail(config.senderEmail, config.receiverEmail, text)
server.quit()
