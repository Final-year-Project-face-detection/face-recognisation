from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('mark/', views.markAttendance, name="markattendence"),
    path('accounts/login/', views.loginView, name="login"),
    path('logout', views.logoutView, name="logout"),
    path('livecam', views.livecam_feed, name='livecam'),
]