from django.urls import path, include
from . import views
from h_apps.views import about,Contact
from django.contrib import admin
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('index1/', views.index1, name='index1'),
    path('contact/', views.contact, name='contact'),
]

