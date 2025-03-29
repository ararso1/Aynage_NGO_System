from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.http import JsonResponse
from django.utils import timezone
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Max, F

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
    return render(request, 'vacancy.html', {'vac':vac})

def signin(request):
    return render(request, 'login.html')

def donate(request):
    return render(request, 'donate.html')

def vacancy_details(request):
    return render(request, 'vacancy details.html')

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

<<<<<<< HEAD
=======

def dashboard_view(request):
    return render(request, 'admin_page/dashboard.html')

def blogs_view(request):
    return render(request, 'admin_page/blogs_post.html')

def vacancy_post_view(request):
    return render(request, 'admin_page/vacancy_post.html')

def logout_view(request):
    return render(request, 'admin_page/logout.html')




# Category
category_list = Category.objects.exclude(status = 2).all()
context = {
    'page_title' : 'Simple Blog Site',
    'category_list' : category_list,
    'category_list_limited' : category_list[:3]
}
>>>>>>> fd99e692ce026c963769eb85cccbdb876d297fca

def admin_dashboard(request):
    blog_count = Blog.objects.count()
    vacancy_count = Vacancy.objects.count()

    # Initialize variables for last updates
    last_blog_update = "No updates yet"
    last_vacancy_update = "No updates yet"

    # Check if there are any blog entries before aggregating
    if blog_count > 0:
        last_blog_update = Blog.objects.aggregate(last_updated=Max('updated_at'))['last_updated']
        if last_blog_update is None:
            last_blog_update = "No updates yet"

    # Check if there are any vacancy entries before aggregating
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


# vacancy part
def vacancy_list(request):
    vacancies = Vacancy.objects.all().order_by('-created_at') 
    return render(request, 'admin_page/vacancy_list.html', {'vacancies':vacancies})

def create_vacancy(request):
    if request.method == "POST":
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('vacancy_list')  # Update with your vacancy list URL name
    else:
        form = VacancyForm()
    
    return render(request, 'admin_page/create_vacancy.html', {'form': form})

# @login_required
def update_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES, instance=vacancy)
        if form.is_valid():
            vacancy = form.save(commit=False)
            # blog.updated_by = request.user  # Set the user who last updated the blog
            vacancy.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=vacancy)
    
    return render(request, 'admin_page/edit_vacancy.html', {'form': form, 'vacancy': vacancy})

def delete_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    if request.method == "POST":
        vacancy.delete()
        return redirect('vacancy_list')  # Adjust to your blog list view name
    return redirect('vacancy_list')


# blog part
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')  # Fetch blogs ordered by newest first
    return render(request, 'admin_page/blog_list.html', {'blogs': blogs})

# @login_required
def create_blogs(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            # blog.added_by = request.user  # Set the user who created the blog
            # blog.updated_by = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'admin_page/create_blog.html', {'form': form})

# @login_required
def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            # blog.updated_by = request.user  # Set the user who last updated the blog
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
    
    return render(request, 'admin_page/edit_blog.html', {'form': form, 'blog': blog})

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        blog.delete()
        return redirect('blog_list')  # Adjust to your blog list view name
    return redirect('blog_list')

def profile_view(request):
    return render(request, 'admin_page/profileview.html')

def profile_update(request):
    return render(request, 'admin_page/profileupdate.html')