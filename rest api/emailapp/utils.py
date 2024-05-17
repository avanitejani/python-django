
# geeks for geeks in site pr thi copy kyro  

from django.conf import settings  # stting je email setting  no code 6e lakhelo te use krva mate
from django.core.mail import send_mail, EmailMessage   #aanathi mail send thase ,EmailMessage: thi file attech krva


def send_mail_to_client():
    subject = 'welcome my world'
    message = 'Hi , thank you for registering in erth ' 
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mithitejano80@gmail.com']  #jemne moklvu hoi temni id
    # recipient_list = ['atejani72@gmail.com']  #jemne moklvu hoi temni id

    send_mail( subject, message, email_from, recipient_list )



def mail_with_file(filepath):
    subject = 'welcome my world'
    message = 'Hi , thank you for registering in erth ' 
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['avanitejani@gmail.com']  #jemne moklvu hoi temni id
    # recipient_list = ['atejani72@gmail.com']  #jemne moklvu hoi temni id
    user =EmailMessage(subject=subject,body=message,from_email=email_from,to=recipient_list)
    user.attach_file(filepath)
    user.send()

# pela ma send_mail ma krta m aama EmailMessage ma badhu pass krvanu with path 