import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import formatdate
from email import encoders

class Email:
  
  
  def __init__(email, password, 
               addresses, subject,
               files = False, text):
      this.email = email #sending email String
      this.pass = password #sending email pass String
      this.addresses = addresses #List of Email Addresses in Strings
      this.subject = subject #subject headed String
      this.files = files #the location of files to be attatched List of Strings
      this.text = text #text to be sent String
    
  def send_email( this, sendTo):

      msg=MIMEMultipart()
      msg['From']= this.email
      msg['To']= sendTo
      msg['Date']= formatdate(localtime=True)
      msg['Subject']= this.subject

      msg.attach(MIMEText, 'plain')
      if this.files != False:
          for f in this.files or []:
              with open(f, "rb") as fil:
                  part = MIMEApplication(
                  fil.read(),
                  Name=basename(f)
                  )  
      # After the file is closed
              part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
              msg.attach(part)
      server.sendmail( this.email, sendTo, this.text)



  def format_emails(this):

      server=smtplib.SMTP('smtp.gmail.com',587)
      server.starttls()
      server.login(this.email, this.password)

      for i in this.addresses:
          send_email(sendTo = i)
      
      server.quit()

