from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpAPIView.as_view(), name='user-signup'),
    path('login/', views.LoginAPIView.as_view(), name='user-login'),
#    path('like/<int:blog_id>/', views.LikeToggleAPIView.as_view(), name='favourites'),
#    path('bookmark/<int:blog_id>/', views.BookmarkToggleAPIView.as_view(), name='reading-list'),
    path('likedblogs/', views.LikedBlogsAPIView.as_view(), name='liked-blogs'),
    path('bookmarkedblogs/', views.BookmarkedBlogsAPIView.as_view(), name='bookmarked-blogs'),
    path('favourite/<int:blog_id>/', views.FavouriteToggleAPIView.as_view(), name='favourites'),
    path('favblogs/', views.FavouritesListAPIView.as_view(), name='favourites-list'),
]