import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

def send_email(email='str',password='str', send_to_email='str',
               subject='str',message='str'):

    msg=MIMEMultipart()
    msg['From']=email
    msg['To']=send_to_email
    msg['Subject']=subject

    msg.attach(MIMEText, 'plain')

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,send_to_email,text)
    server.quit()

file_location='C:\\the_location_of\\your_file'
filename= os.path.basename(file_location)
email='youremail@gmail.com'
pas='password'
sybject='Subject title'
addresses=['emailaddress@live.com','emailaddress@gmail.com']
message='text or file upload'
for i in addresses:
    send_email(email=email,password=pas, send_to_email=i,
               subject=subject,message=message)

