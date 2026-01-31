from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Blog
from .serializers import BlogSerializer

@api_view(['GET', 'POST'])
def blog_list(request):
    """
    FRONTEND USAGE:
    
    1. FILTERING (Search Bar):
       URL: /api/blogs/?search=python
       Behavior: Finds 'python' in Title, Content, Category, or Tags.
       
    2. FILTERING (Sidebar Topics):
       URL: /api/blogs/?category=Tech
       Behavior: Returns ONLY blogs with category="Tech".
       
    3. CREATE BLOG:
       Method: POST
       Data: { "title": "...", "content": "...", "category": "Tech", "tags": ["coding"] }
    """
    if request.method == 'GET':
        queryset = Blog.objects.all()

        # 1. Search Logic
        search_query = request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(content__icontains=search_query) |
                Q(category__icontains=search_query) |
                Q(tags__name__icontains=search_query)
            ).distinct()

        # 2. Category Filter
        category_query = request.query_params.get('category', None)
        if category_query:
            queryset = queryset.filter(category=category_query)

        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def blog_detail(request, pk):
    """
    FRONTEND USAGE:
    URL: /api/blogs/1/
    Returns: The full blog object for the Detail Page.
    """
    blog = get_object_or_404(Blog, pk=pk)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

@api_view(['POST'])
def toggle_like(request, pk):
    """
    FRONTEND USAGE:
    URL: /api/blogs/1/like/
    Method: POST (No data needed)
    Returns: { "status": "liked", "like_count": 1 }
    Note: Use 'like_count' to update the number next to the heart icon instantly.
    """
    blog = get_object_or_404(Blog, pk=pk)
    if request.user in blog.likes.all():
        blog.likes.remove(request.user)
        return Response({"status": "unliked", "like_count": blog.likes.count()})
    blog.likes.add(request.user)
    return Response({"status": "liked", "like_count": blog.likes.count()})

@api_view(['POST'])
def toggle_star(request, pk):
    """
    FRONTEND USAGE:
    URL: /api/blogs/1/star/
    Method: POST
    """
    blog = get_object_or_404(Blog, pk=pk)
    if request.user in blog.stars.all():
        blog.stars.remove(request.user)
        return Response({"status": "unstarred"})
    blog.stars.add(request.user)
    return Response({"status": "starred"})

@api_view(['POST'])
def toggle_bookmark(request, pk):
    """
    FRONTEND USAGE:
    URL: /api/blogs/1/bookmark/
    Method: POST
    """
    blog = get_object_or_404(Blog, pk=pk)
    if request.user in blog.bookmarks.all():
        blog.bookmarks.remove(request.user)
        return Response({"status": "unbookmarked"})
    blog.bookmarks.add(request.user)
    return Response({"status": "bookmarked"})