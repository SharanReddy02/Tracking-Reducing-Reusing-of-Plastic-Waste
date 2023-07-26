"""vyarth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path('^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path('^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  re_path('^blog/', include('blog.urls'))
"""
"from django.conf.urls import url,patterns"
from django.urls import include, re_path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    re_path('^admin/', admin.site.urls),
    re_path("^$", views.HomePage.as_view(), name="home"),
    re_path("^login/$", auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    re_path("^logout/$", auth_views.LogoutView.as_view(), name="logout"),
    re_path("^signup/$", views.SignUp.as_view(), name="signup"),
    re_path("^gview/$", views.GenView.as_view(), name="gview"),
    re_path("^cview/$", views.ColView.as_view(), name="cview"),
    re_path('^result/$',views.Result.as_view(),name='result'),
    re_path("^new_view/$", views.new_view, name="new_view"),

]
