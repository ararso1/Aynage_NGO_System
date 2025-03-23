from django.shortcuts import render,redirect
from .models import Category, Blog, User
from django.http import JsonResponse
from django.utils import timezone
from .forms import BlogForm
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

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

# Admin panel
def admin_panel(request):
    return render(request, 'admin_page/index.html')

def vacancy_list(request):
    return render(request, 'admin_page/vacancy_list.html')

def admin_dashboard(request):
    return render(request, 'admin_page/dashboard.html')

def blog_list(request):
    categories = Category.objects.all()
    return render(request, 'admin_page/blog_list.html', {'categories': categories})

def create_blogs(request):
    return render(request, 'admin_page/create_blog.html')

def create_vacancy(request):
    return render(request, 'admin_page/create_vacancy.html')


def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # Set the author to the current logged-in user
            blog.save()
            return JsonResponse({'success': True})  # Indicate success
        else:
            # Convert form errors to a dictionary
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = error_list[0]  # Only return the first error for each field
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)