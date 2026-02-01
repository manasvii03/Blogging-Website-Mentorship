from django.contrib import admin
from .models import Blog, Tag  

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'created_at') 
    readonly_fields = ('created_at', 'updated_at', 'read_time')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)