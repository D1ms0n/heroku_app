from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    driver = webdriver.PhantomJS()
    driver.set_window_size(1120, 550)
    driver.get("http://instagram.com/")
    
    a = driver.find_elements_by_css_selector('button')
    b = len(a)
    
    
    
    return render(request, 'index.html', {'b': b})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

