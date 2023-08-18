from pyexpat import model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from PIL import Image
from datetime import datetime
import os


class Ticket(models.Model):
    title = models.CharField(max_length=128, verbose_name='Titre')
    description = models.TextField(
        max_length=2048, blank=True, verbose_name='Description')
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    has_review = models.BooleanField(default=False)

    IMAGE_MAX_SIZE = (500, 500)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def image_exists(self):
        if self.image and os.path.exists(self.image.path):
            return True
        return False

    def formatted_time_created(self):
        return self.time_created.strftime("%H:%M, %d %B %Y")

    @property
    def is_ticket(self):
        return True

    def get_review(self):
        try:
            return self.review_set.get()
        except Review.DoesNotExist:
            return None


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    RATING_CHOICES = (
        (0, '- 0'),
        (1, '- 1'),
        (2, '- 2'),
        (3, '- 3'),
        (4, '- 4'),
        (5, '- 5'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Note")
    headline = models.CharField(max_length=128, verbose_name="Titre")
    body = models.TextField(max_length=8192, blank=True,
                            verbose_name="Commentaire")
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def formatted_time_created(self):
        return self.time_created.strftime("%H:%M, %d %B %Y")

    def rating_display(self):
        if self.rating in range(1, 6):
            return '⭐' * self.rating
        else:
            return str(self.rating)

    @property
    def is_review(self):
        return True


class UserFollows(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following'
    )
    followed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by'
    )

    class Meta:
        unique_together = ('user', 'followed_user')
