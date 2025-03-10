import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email = "rafael.honorato03@gmail.com"

#instancia do MIMEMultipart
msg = MIMEMultipart()

msg["From"] = email
msg["To"] = email
msg["Subject"] = "Teste de envio de e-mail com anexo"

body = "Teste de envio de e-mail com anexo"

msg.attach(MIMEText(body, "plain"))

s = smtplib.SMTP("smtp.gmail.com", 587)

s.starttls()

s.login(fromaddr, 'robos123')

TEXT = msg.as_string()

s.sendmail(email, email, TEXT)
