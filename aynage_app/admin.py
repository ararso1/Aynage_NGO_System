from django.contrib import admin
from .models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'added_by', 'updated_by', 'created_at', 'updated_at')
    list_filter = ('status', 'categories')
    search_fields = ('title', 'slug', 'description')
    filter_horizontal = ('categories',)
    readonly_fields = ('slug', 'added_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        if not change or not obj.added_by:
            obj.added_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(User)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Vacancy)
admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Category)

