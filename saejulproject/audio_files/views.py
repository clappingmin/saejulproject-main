from django.views.generic.edit import CreateView
from audio_recorder.views import AudioFileCreateViewMixin
from .models import AudioFile
from .forms import AudioFileForm

from django import http
from django.views.generic.base import View


class AudioFileCreateViewMixin(View):
    model = None
    create_field = None

    def create_object(self, audio_file):
        return self.model.objects.create(**{self.create_field: audio_file})

    def post(self, request):
        audio_file = request.FILES.get('audio_file', None)

        if audio_file is None:
            return http.HttpResponseBadRequest()

        result = self.create_object(audio_file)
        # print result.audio_file.url
        return http.JsonResponse({
            'id': result.pk,
            'url': result.audio_file.url,
        }, status=201)



class AudioFileAPICreateView(AudioFileCreateViewMixin):
    model = AudioFile


class AudioFileCRUDCreateView(CreateView):
    model = AudioFile
    form_class = AudioFileForm
