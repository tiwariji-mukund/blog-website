from django.contrib import admin
from .models import Post, Category, UserProfile, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Comment)

