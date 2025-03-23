from . import views
from django.urls import path
from django.conf.urls import handler404
from .views import custom_404

handler404 = custom_404

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('blogs', views.blogs, name='blogs'),
    path('contact', views.contact, name='contact'),
    path('climate', views.climate, name='climate'),
    path('our_work', views.our_work, name='our_work'),
    path('why_donate', views.why_donate, name='why_donate'),
    path('vacancy', views.vacancy, name='vacancy'),
    path('signin', views.signin, name='signin'),
    path('donate', views.donate, name='donate'),
    path('vacancy_details', views.vacancy_details, name='vacancy_details'),
    # Admin panel
    # path('category_mgt',views.category_mgt,name='category-mgt'),
    # path('manage_category',views.manage_category,name='manage-category'),
    # path('categories',views.categories,name='category-page'),
    path('admin_dashboard',views.admin_dashboard,name='admin_panel'),
    path('blog_list', views.blog_list, name='blog_list'),
    path('vacancy_list', views.vacancy_list, name='vacancy_list'),
    path('create_blog/', views.create_blogs, name='create_blog'),
    path('create_vacancy/', views.create_vacancy, name='create_blog'),

]