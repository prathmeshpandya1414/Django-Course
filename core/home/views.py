from django.shortcuts import render

from django.http import HttpResponse
from vegge.seed import *
from .utils import send_email_to_client, send_email_with_attachment
from django.conf import settings
from .models import *

def send_email(request):
    # send_email_to_client()
    
    subject = "This email is from Django server with attachment"
    message = "This is test message from Django with attachment"
    recipent_list = ["ph.pandya1414@gmail.com"]
    file_path = f"{settings.BASE_DIR}/core/curd&shell_activites.txt"
    send_email_with_attachment(subject, message, recipent_list, file_path)
    return HttpResponse("Email sent successfully")
    return redirect('/')
    



def home(request):
    # seed_db(100)

    Car.objects.create(car_name=f"BMW-{random.randint(0,250)}")


    peoples = [
        {'name': 'gyansingh tomar', 'age': 12},
        {'name': 'harijeet singh', 'age': 15},
        {'name': 'samir shah', 'age': 45},
        {'name': 'ranveer singh', 'age': 28},
        {'name': 'varun das', 'age': 27}
    ]
    # vegetables=  ["pumkin","potato","tomato"]  # type: ignore

    return render(request, "home/index.html", context = {'page': 'Django Tutorial','peoples':peoples})     
    
def about(request):
    context =  {'page': 'About'}
    return render(request, "home/about.html", context)
def contact(request):
    context =  {'page': 'Contact'}
    return render(request, "home/contact.html", context)
def success_page(request):
    print("#" *10)
    return HttpResponse("<h1>Hey wassup succes page</h1>")
