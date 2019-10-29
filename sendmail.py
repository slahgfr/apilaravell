
#!/usr/bin/python
 
import smtplib
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
msg = MIMEMultipart('mixed')
 
msg['Subject'] = 'test  de messagerie TPIMAIL'
msg['From']    = 'sender@babnet.com'
msg['To']      = 'slah.ghanmi@promessa.com'
html = 'message au format html'
text = 'message au format texte'
 
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
 
username = 'test'
password = 'b8b2d9c5a55984b9dfd5572df413be9c'
 
msg.attach(part1)
msg.attach(part2)
 
s = smtplib.SMTP('smtp.gmail.com', 993)
s.set_debuglevel(1)
s.startssll()
 
s.login(username, password)
 
 
try:
    s.sendmail(msg['From'], msg['To'], msg.as_string())
finally:
    s.quit()
