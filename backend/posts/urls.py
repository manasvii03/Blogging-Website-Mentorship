from django.urls import path
from .views import blog_list, blog_detail, toggle_like, toggle_star, toggle_bookmark

urlpatterns = [
    # 1. The Feed & Creation
    path('blogs/', blog_list, name='blog-list'),

    # 2. Single Blog Details
    path('blogs/<int:pk>/', blog_detail, name='blog-detail'),

    # 3. Interactions (Buttons)
    path('blogs/<int:pk>/like/', toggle_like, name='toggle-like'),
    path('blogs/<int:pk>/star/', toggle_star, name='toggle-star'),
    path('blogs/<int:pk>/bookmark/', toggle_bookmark, name='toggle-bookmark'),
]