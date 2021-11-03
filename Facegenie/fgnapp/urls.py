from django.urls import path, include
from fgnapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.handleSignup, name='signup'),
    path('login/', views.handlelogin, name='loggingin'),
    path('logout/', views.handlelogout, name='loggingout')
]
