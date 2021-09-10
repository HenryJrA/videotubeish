from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Video
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView

class Index(ListView):
  model = Video
  template_name = 'videos/index.html'
  order_by = '-date_posted'

class CreateVideo( LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'description', 'thumbnail', 'videoFile']
    template_name = 'videos/createvideo.html'
 

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})

class DetailVideo(LoginRequiredMixin, DetailView):
    model = Video
    template_name = "videos/detailvideo.html"

class UpdateVideo (LoginRequiredMixin, UpdateView):
  model =  Video
  fields = ['title', 'description']
  template_name = 'videos/createvideo.html'

  def get_success_url(self):
      return reverse('video-detail', kwargs={'pk': self.object.pk})


class DeleteVideo(LoginRequiredMixin, DeleteView):
	model = Video
	template_name = 'videos/deletevideo.html'

	def get_success_url(self):
		return reverse('index')
	
