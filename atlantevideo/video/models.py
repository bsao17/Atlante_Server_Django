from django.db import models

class Video (models.Model):
    video_link = models.CharField(max_length=255, default=0)
    video_time = models.CharField(max_length=255, default=0)
    video_title = models.CharField(max_length=255, default=0)
    videographer = models.CharField(max_length=255, default=0)
    video_location = models.CharField(max_length=255, default=0)

class Videographer (models.Model):
    name = models.CharField(max_length=255, default=0)
    age = models.IntegerField(default=0)
    country = models.CharField(max_length=255, default=0)
    speciality = models.CharField(max_length=255, default=0)