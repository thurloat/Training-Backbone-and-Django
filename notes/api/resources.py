from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from notes.models import Note

class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        authorization = Authorization()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get']
