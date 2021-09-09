from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.detail import Detailview
from .models import Video

# Create your views here.

def index(request):
  return render(request, 'videos/index.html')

class CreateVideo(CreateView):
    model = Video
    fields = ['title', 'description', 'thumbnail', 'videoFile']
    template_name = 'videos/createvideo.html'

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})

class DetailVideo(Detailview):
    model = Video
    template_name = "videos/videodetail.html"
