from django.contrib import admin
from django.urls import path
from accounts.views import create_profile, home, signup, logout_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('profile/', create_profile, name="profile"),
    path('signup/', signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
]