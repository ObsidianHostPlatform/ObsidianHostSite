from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('features.html', views.features, name='features'),
    path('pricing.html', views.pricing, name='pricing'),
    path('contact.html', views.contact, name='contact'),
    path('login.html', views.login, name='login'),
    path('profile.html', views.profile, name='profile'),
    path('register.html', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),

]
