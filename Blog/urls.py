from django.urls import path
from .views import PostsList, PostDetail

urlpatterns = [
    path('blog/posts/', PostsList.as_view(), name='item-list'),
    path('blog/posts/<int:pk>/', PostDetail.as_view(), name='post'),
]