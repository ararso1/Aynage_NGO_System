from django.shortcuts import render
from .models import Category, Post
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
    return render(request, 'vacancy.html')

def signin(request):
    return render(request, 'login.html')

def donate(request):
    return render(request, 'donate.html')

def vacancy_details(request):
    return render(request, 'vacancy details.html')

def admin_panel(request):
    return render(request, 'admin_page/index.html')


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

def category_mgt(request):
    categories = Category.objects.all()
    context['page_title'] = "Category Management"
    context['categories'] = categories
    return render(request, 'admin/category_mgt.html', context)

def manage_category(request,pk=None):
    # category = Category.objects.all()
    if pk == None:
        category = {}
    elif pk > 0:
        category = Category.objects.filter(id=pk).first()
    else:
        category = {}
    context['page_title'] = "Manage Category"
    context['category'] = category

    return render(request, 'admin/manage_category.html',context)

def categories(request):
    categories = Category.objects.filter(status = 1).all()
    context['page_title'] = "Category Management"
    context['categories'] = categories
    return render(request, 'admin/categories.html',context)

