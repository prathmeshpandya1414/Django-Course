from django.shortcuts import render

from django.http import HttpResponse

def home(request):
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
