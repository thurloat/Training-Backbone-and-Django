from tastypie.api import Api
from resources import NoteResource

v1 = Api("v1")
v1.register(NoteResource())
