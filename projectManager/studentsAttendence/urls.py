from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('camselect/', views.camselect, name='camselect'),
    path('mark/', views.markAttendance, name="markattendence"),
    path('accounts/login/', views.loginView, name="login"),
    path('logout', views.logoutView, name="logout"),
    path('livecam', views.livecam_feed, name='livecam'),
    path('status', views.status, name='status'),
    path('pdf_view/', views.ViewPDF, name="pdf_view"),
    path('pdf_download/', views.DownloadPDF, name="pdf_download"),
]


from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)