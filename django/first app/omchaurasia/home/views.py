from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        "variable":"This is sent"
    }
    
    
    return render(request,"index.html", context)
def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        contact = Contact(name=name , message=message)
        contact.save()
        messages.success(request,  'Your form has been submitted!')
    return render(request, "contact.html")
