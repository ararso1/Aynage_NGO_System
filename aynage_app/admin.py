from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Vacancy)
admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Category)

