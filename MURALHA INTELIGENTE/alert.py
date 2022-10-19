import smtplib
from email.message import EmailMessage
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
#from contextlib import asynccontextmanager
#import asyncio

#@asynccontextmanager
#async def run_in_background(email_alert):
#    task = asyncio.create_task(email_alert)
#    try:
#        yield task
#    finally:
#        await task

def email_alert(subject, to, frameIndex):
    msg = MIMEMultipart()

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    
    user = "mii.santos342@gmail.com"
    password = "txwoiyregrehghsp"

    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user
    
    with open('output/frame-{}.png'.format(frameIndex), 'rb') as fp:
        img = MIMEImage(fp.read())
    msg.attach(img)
    
    server.login(user, password)
    server.send_message(msg)
    server.close()

#if __name__ == '__main__':
#    email_alert("teste", "testando envio de emails por python", "cantora_mylena@hotmail.com")