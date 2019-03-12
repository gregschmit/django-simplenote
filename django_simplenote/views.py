from django.views import generic
from . import models


class NoteView(generic.CreateView):
    model = models.Note
    template_name = 'simplenote/note.html'
    fields = ['content']
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['notes'] = models.Note.objects.all()
        return context
