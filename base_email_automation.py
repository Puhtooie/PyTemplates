import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email import encoders

'''
Microsoft word= .docx
OpenDocument Format=.odt
Rich Text Format= .rft
PDF Document= .pdf
Plain Text= .txt
change gmail to less secure
'''


class autoEmail:

    def __init__(self, email, pswd, subject, message, addresses,file_loc = 'na'):

        self.email = email
        self.pswd = pswd
        self.subj = subject
        self.msg = message
        #addresses in list 
        self.adrs = addresses 
        if file_loc != 'na':
            self.files = [False]
        else:
            self.files= file_loc

    def send_email(self,send_to='str'):

        msg=MIMEMultipart()
        msg['From']=self.email
        msg['To']=send_to
        msg['Date']= formatdate(localtime=True)
        msg['Subject']=self.subject

        msg.attach(MIMEText(self.text, 'plain'))
        if self.files[0] != False:
            for f in self.files or []:
                with open(f, "rb") as fil:
                    part = MIMEApplication(
                    fil.read(),
                    Name=basename(f)
                    )  
        # After the file is closed
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
                msg.attach(part)

        text=msg.as_string()

        server.sendmail(self.email,send_to,self.text)

    def format_email():
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(self.email,self.pswd)

        for i in self.adrs:
            self.send_email(send_to=i)
        server.quit()


