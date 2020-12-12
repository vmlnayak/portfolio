from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.Home,name='home'),
    path('contact/',views.Contact,name='contact'),
    path('media/',views.Media,name='media'),
    path('achievement/',views.Achievement,name='achievement'),
    path('login/', auth_views.LoginView.as_view(template_name="base/login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
]
