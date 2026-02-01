from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Blog, Tag
from .serializers import BlogSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def blog_list(request):
    if request.method == 'GET':
        queryset = Blog.objects.all().prefetch_related('tags', 'likes', 'stars', 'bookmarks')
        search_query = request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query) |
                Q(category__icontains=search_query) | Q(tags__name__icontains=search_query)
            ).distinct()
        category_query = request.query_params.get('category')
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
    blog = get_object_or_404(Blog, pk=pk)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_like(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
        return Response({"status": "unliked", "like_count": blog.likes.count()})
    blog.likes.add(request.user)
    return Response({"status": "liked", "like_count": blog.likes.count()})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_star(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.stars.filter(id=request.user.id).exists():
        blog.stars.remove(request.user)
        return Response({"status": "unstarred", "star_count": blog.stars.count()})
    blog.stars.add(request.user)
    return Response({"status": "starred", "star_count": blog.stars.count()})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_bookmark(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.bookmarks.filter(id=request.user.id).exists():
        blog.bookmarks.remove(request.user)
        return Response({"status": "unbookmarked"})
    blog.bookmarks.add(request.user)
    return Response({"status": "bookmarked"})