from django.contrib import admin
from django.urls import path
from accounts.views import create_profile, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('profile/', create_profile, name="profile"),
]