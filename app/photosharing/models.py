from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone

fs = FileSystemStorage(location=settings.MEDIA_ROOT)


class Team(models.Model):
    owner = models.ForeignKey(User, related_name='team_owner', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='team_members', blank=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=250, blank=True)
    logo = models.ImageField(upload_to=settings.MEDIA_URL, storage=fs, blank=True, null=True)
    establish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("photosharing:team_details", kwargs={"pk": self.pk})


class Photo(models.Model):
    uploaded_to = models.ForeignKey(Team, on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to=settings.MEDIA_URL, storage=fs, blank=True, null=True)
    public = models.BooleanField(default=False)
    description = models.CharField(max_length=200, blank=True, null=True)

