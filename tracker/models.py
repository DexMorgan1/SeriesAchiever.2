from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    poster_path = models.URLField(max_length=500, blank=True, null=True)
    tmdb_id = models.IntegerField(unique=True) 

class Episode(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='episodes')
    season_number = models.IntegerField()
    episode_number = models.IntegerField()
    name = models.CharField(max_length=255)
    watched = models.BooleanField(default=False) 
