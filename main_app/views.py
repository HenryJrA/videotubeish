from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Video

from django.views.generic.list import ListView

class Index(ListView):
  model = Video
  template_name = 'videos/index.html'
  order_by = '-date_posted'

class CreateVideo( CreateView):
    model = Video
    fields = ['title', 'description', 'thumbnail', 'videoFile']
    template_name = 'videos/createvideo.html'


    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})

class DetailVideo(DetailView):
    model = Video
    template_name = "videos/detailvideo.html"

class UpdateVideo (UpdateView):
  model =  Video
  fields = ['title', 'description']
  template_name = 'videos/createvideo.html'

  def get_success_url(self):
      return reverse('video-detail', kwargs={'pk': self.object.pk})


class DeleteVideo( DeleteView):
	model = Video
	template_name = 'videos/deletevideo.html'

	def get_success_url(self):
		return reverse('index')
	
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'tubeish'