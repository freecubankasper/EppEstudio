import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.template.loader import render_to_string

from epp import settings


def send_email(estado,nombre):
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado...')

        email_to = 'laconsulrenta@gmail.com'
        # Construimos el mensaje simple
        mensaje = MIMEText("""Hi %s,

Your project %s.
If you dont know how to fix this, please contact it-support.

Best regards
Your friendly Estudio50habana TEAM""" % (email_to,nombre))
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = "Tienes un correo"

        mailServer.sendmail(settings.EMAIL_HOST_USER, email_to, mensaje.as_string())
    except Exception as e:
        print(e)
def send_email_contact(first_name,last_name,email,phone,budget,message):
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado...')

        email_to = settings.EMAIL_HOST_USER
        # Construimos el mensaje simple
        mensaje = MIMEMultipart()
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = "Tienes un correo"

        content = render_to_string('envio_correo.html', {'first_name': first_name + last_name,'message': message})
        mensaje.attach(MIMEText(content, 'html'))

        mailServer.sendmail(settings.EMAIL_HOST_USER, email_to, mensaje.as_string())
        print('Correo enviado correctamente')
    except Exception as e:
        print(e)

def send_email_proyecto(usuario, nombre, categoriahtml):
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado...')
        email_to = settings.EMAIL_HOST_USER
        # Construimos el mensaje simple
        mensaje = MIMEMultipart()
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = "Tienes un correo"

        content = render_to_string('envio_correo.html', {'first_name': usuario.first_name + usuario.last_name,'message': nombre + categoriahtml})
        mensaje.attach(MIMEText(content, 'html'))

        mailServer.sendmail(settings.EMAIL_HOST_USER, email_to, mensaje.as_string())
        print('Correo enviado correctamente')
    except Exception as e:
        print(e)
