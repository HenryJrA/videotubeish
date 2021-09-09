from django.contrib import admin
from django.urls import path
from .views import CreateVideo, DetailVideo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('create/', CreateVideo.as_view(), name='video-create'),
  path('<int:pk>/', DetailVideo.as_view(), name='video-detail') 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
