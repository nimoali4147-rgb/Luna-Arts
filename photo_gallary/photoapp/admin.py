from django.contrib import admin
from .models import Tag, Photo, PhotoReaction

admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(PhotoReaction)