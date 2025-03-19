from . import views
from django.urls import path

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
    #Admin panel
    # path('category_mgt',views.category_mgt,name='category-mgt'),
    # path('manage_category',views.manage_category,name='manage-category'),
    # path('categories',views.categories,name='category-page'),
    path('admin_panel',views.admin_panel,name='admin-page'),

]