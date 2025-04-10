from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import JsonResponse
from django.utils import timezone
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Max, F
from django.contrib.auth import logout

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blogs(request):
    return render(request, 'blogs.html')

def contact(request):
    return render(request, 'contact.html')

def climate(request):
    return render(request, 'climate.html')

def our_work(request):
    return render(request, 'our_work.html')

def why_donate(request):
    return render(request, 'why_donate.html')

def vacancy(request):
    vac = Vacancy.objects.all().order_by('-created_at')
    return render(request, 'vacancy.html', {'vac': vac})

def signin(request):
    return render(request, 'login.html')

def donate(request):
    return render(request, 'donate.html')

def vacancy_details(request):
    return render(request, 'vacancy_details.html')

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

def admin_dashboard(request):
    blog_count = Blog.objects.count()
    vacancy_count = Vacancy.objects.count()

    last_blog_update = "No updates yet"
    last_vacancy_update = "No updates yet"

    if blog_count > 0:
        last_blog_update = Blog.objects.aggregate(last_updated=Max('updated_at'))['last_updated']
        if last_blog_update is None:
            last_blog_update = "No updates yet"

    if vacancy_count > 0:
        last_vacancy_update = Vacancy.objects.aggregate(last_updated=Max('updated_at'))['last_updated']
        if last_vacancy_update is None:
            last_vacancy_update = "No updates yet"

    return render(request, 'admin_page/dashboard.html', {
        'blog': blog_count,
        'vacancy': vacancy_count,
        'last_blog': last_blog_update,
        'last_vacancy': last_vacancy_update
    })

# Vacancy part
def vacancy_list(request):
    vacancies = Vacancy.objects.all().order_by('-created_at')
    return render(request, 'admin_page/vacancy_list.html', {'vacancies': vacancies})

def create_vacancy(request):
    if request.method == "POST":
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm()
    
    return render(request, 'admin_page/create_vacancy.html', {'form': form})

def update_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm(instance=vacancy)
    
    return render(request, 'admin_page/edit_vacancy.html', {'form': form, 'vacancy': vacancy})

def delete_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    if request.method == "POST":
        vacancy.delete()
        return redirect('vacancy_list')
    return redirect('vacancy_list')

# Blog part
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'admin_page/blog_list.html', {'blogs': blogs})

def create_blogs(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'admin_page/create_blog.html', {'form': form})

def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    
    return render(request, 'admin_page/edit_blog.html', {'form': form, 'blog': blog})

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        blog.delete()
        return redirect('blog_list')
    return redirect('blog_list')

# Profile-related views
def profile_view(request):
    return render(request, 'admin_page/profileview.html')

def profile_update(request):
    return render(request, 'admin_page/profileupdate.html')

# Admin profile views
def profile(request):
    return render(request, 'admin_page/profile.html')

def profile_edit(request):
    return render(request, 'admin_page/profileedit.html')

# Dashboard views
def dashboard_view(request):
    return render(request, 'admin_page/dashboard_view.html')

def blogs_view(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'admin_page/blogs_view.html', {'blogs': blogs})

def vacancy_post_view(request):
    vacancies = Vacancy.objects.all().order_by('-created_at')
    return render(request, 'admin_page/vacancy_post_view.html', {'vacancies': vacancies})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')
