from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable1' : 'I am the variable value',
        'variable2' : 'I am successfully rendered'
    }
    return render(request, 'index.html', context)
    # return HttpResponse('this is home page')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('this is about page')

def chocolate(request):
    return render(request, 'chocolate.html')
    # return HttpResponse('this is services page')

def icecream(request):
    return render(request, 'icecream.html')

def bakery(request):
    return render(request, 'bakery.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
    # return HttpResponse('this is contact page')


