from django.contrib import admin
from .models import *
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'description')


admin.site.register(UserProfile, UserProfileAdmin)


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = ('title', 'category', 'created_at')


admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(Category,CategoryAdmin)