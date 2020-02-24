"""HBT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotelapp import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('signup/', views.signup),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view(template_name='index.html')),
    path('profile/', views.profile),
    path('rooms/', views.rooms),
    path('rooms/register/<int:id>/', views.register),
    path('congrats/', views.congrats),
    path('about/', views.about)

]
