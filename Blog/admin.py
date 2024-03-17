from django.contrib import admin
from Blog.models import Post
from accounts.models import AppUser


class Members(admin.ModelAdmin):
    list_display = ('username', 'email', 'joined_date')
admin.site.register(Post)
admin.site.register(AppUser, Members)