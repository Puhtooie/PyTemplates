import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import formatdate
from email import encoders

def send_email(email='str',password='str', send_to='str',
               subject='str',message='str',files=[False]):

    msg=MIMEMultipart()
    msg['From']=email
    msg['To']=send_to_email
    msg['Date']= formatdate(localtime=True)
    msg['Subject']=subject

    msg.attach(MIMEText, 'plain')
    if files[0] != False:
        for f in files or []:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                fil.read(),
                Name=basename(f)
                )  
    # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)


    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,send_to,text)
    server.quit()

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,send_to,text)
    server.quit()

file_locations=['C:\\the_location_of\\your_file',
               'C:\\the_location_of\\your_2nd_file']
email='youremail@gmail.com'
pas='password'
subject='Subject title'

addresses=['intended_emails@mail.com']

message='text or file upload'

for i in addresses:
  #if you don't have any attatchments to send makes files=[False]
  send_email(email=email,password=pas, send_to_email=i,
               subject=subject,message=message,files=file_locations)

