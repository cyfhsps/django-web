from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

from . import views

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),##NO SPACE WITHIN THE QUOTE SIGN
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),##NO SPACE WITHIN THE QUOTE SIGN

    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),##NO SPACE WITHIN THE QUOTE SIGN
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),##NO SPACE WITHIN THE QUOTE SIGN
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),##NO SPACE WITHIN THE QUOTE SIGN
    path('post/new/', PostCreateView.as_view(),name='post-create'),##NO SPACE WITHIN THE QUOTE SIGN
    path('about/', views.about,name='blog-about'),

]
