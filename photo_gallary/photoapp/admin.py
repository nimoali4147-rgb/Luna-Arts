
from django.contrib import admin
from .models import Tag, Photo, PhotoReaction


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'created_at')
    list_filter = ('tags', 'created_at')
    search_fields = ('title', 'description')
    filter_horizontal = ('tags',)


@admin.register(PhotoReaction)
class PhotoReactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'reaction')
    list_filter = ('reaction',)
    search_fields = ('user__username', 'photo__title')
