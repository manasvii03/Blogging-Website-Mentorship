from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpAPIView.as_view(), name='user-signup'),
    path('login/', views.LoginAPIView.as_view(), name='user-login'),
]