from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'aynage/index.html')

def about(request):
    return render(request, 'aynage/about.html')

def blogs(request):
    return render(request, 'aynage/blogs.html')

def contact(request):
    return render(request, 'aynage/contact.html')

def climate(request):
    return render(request, 'aynage/climate.html')

def our_work(request):
    return render(request, 'aynage/our_work.html')

def why_donate(request):
    return render(request, 'aynage/why_donate.html')

def vacancy(request):
    return render(request, 'aynage/vacancy.html')

def signin(request):
    return render(request, 'aynage/login.html')

def donate(request):
    return render(request, 'aynage/donate.html')
