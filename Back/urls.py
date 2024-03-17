from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Blog.urls')),  # Include Blog app
    path('accounts/', include('accounts.urls')), # Include accounts app
]