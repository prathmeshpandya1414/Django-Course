
from home.models import student
import time
from django.core.mail import send_mail, EmailMessage
from django.conf import settings




def run_this_function():
    print("Function Started")
    print("Function Started..")

    time.sleep(2)
    print("Function Executed")

def send_email_to_client():
    subject = "This email is sent from Django"
    message = "This is test message from Django" 
    from_email = settings.EMAIL_HOST_USER
    receipent_list = ["ph.pandya1414@gmail.com"]
    send_mail(subject,message,from_email,receipent_list)

def send_email_with_attachment(subject, message, receipent_list, file_path):
    email = EmailMessage(subject = subject,body = message,from_email=settings.EMAIL_HOST_USER,to = receipent_list)
    email.attach_file(file_path)
    email.send()