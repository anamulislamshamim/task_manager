from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path 
from . import views 
from .forms import LoginForm

app_name = "core" 


urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name="core/login.html", authentication_form=LoginForm), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    
]
