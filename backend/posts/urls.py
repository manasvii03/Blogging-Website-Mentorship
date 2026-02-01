from django.urls import path
from .views import blog_list, blog_detail, toggle_like, toggle_star, toggle_bookmark

# FRONTEND NOTE: API Endpoints
# Base URL: http://127.0.0.1:8000/api/

urlpatterns = [
    # 1. The Feed & Creation
    # GET  /api/blogs/ -> Get all blogs
    # POST /api/blogs/ -> Create a new blog
    path('blogs/', blog_list),

    # 2. Single Blog Details
    # GET /api/blogs/<id>/ -> Get one blog 
    path('blogs/<int:pk>/', blog_detail),

    # 3. Interactions (Buttons)
    # POST /api/blogs/<id>/like/     -> Toggle Like
    # POST /api/blogs/<id>/star/     -> Toggle Star (Favorites)
    # POST /api/blogs/<id>/bookmark/ -> Toggle Bookmark (Reading List)
    path('blogs/<int:pk>/like/', toggle_like),
    path('blogs/<int:pk>/star/', toggle_star),
    path('blogs/<int:pk>/bookmark/', toggle_bookmark),
]