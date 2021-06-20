from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    cover_art = models.URLField(max_length=255)
    release_year = models.CharField(max_length=255, null=True, blank=True)
    
