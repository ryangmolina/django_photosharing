from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from ..photosharing.models import Team


class Invite(models.Model):
    invited = models.ForeignKey(User, related_name='invite_invited', verbose_name='User', on_delete=models.CASCADE)
    inviter = models.ForeignKey(Team, related_name='invite_inviter', on_delete=models.CASCADE)
    invite_date = models.DateTimeField(verbose_name=('created'), default=timezone.now)

    class Meta:
        unique_together = (('invited', 'inviter'),)

    def __str__(self):
        return f'{self.inviter} invited {self.invited}'

    def get_absolute_url(self):
        return reverse('invites:invite_details', kwargs={"pk": self.pk})
