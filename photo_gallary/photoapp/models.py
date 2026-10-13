
from django.conf import settings
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    tags = models.ManyToManyField(
        Tag,
        related_name='photos',
        blank=True
    )
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='uploaded_photos'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PhotoReaction(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'

    REACTION_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='photo_reactions'
    )

    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name='reactions'
    )

    reaction = models.CharField(
        max_length=10,
        choices=REACTION_CHOICES
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'photo'],
                name='unique_user_photo_reaction'
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.photo} - {self.reaction}'
