from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('mark/', views.markAttendence, name="markattendence"),
    path('login/', views.login, name="login"),
    path('livecam_feed', views.livecam_feed, name='livecam_feed'),
]