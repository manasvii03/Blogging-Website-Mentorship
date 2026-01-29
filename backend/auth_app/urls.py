from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpAPIView.as_view(), name='user-signup'),
    path('login/', views.LoginAPIView.as_view(), name='user-login'),
    path('favourites/<int:blog_id>', views.FavouriteToggleAPIView.as_view(), name='favourites'),
    path('readinglist/<int:blog_id>', views.ReadingListAPIView.as_view(), name='reading-list'),
]