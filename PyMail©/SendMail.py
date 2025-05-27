from email.message import EmailMessage
import smtplib


def send(remitente,contraseña,destinatario,asunto,texto):
    """Manda un correo al cual hay que pasarle el/los destinatario/s, un
    asunto y un texto(con el correo y su contraseña de un remitente"""
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = asunto
    email.set_content(texto)
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(remitente, contraseña)
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()