import uuid

from django.db import models
from django.contrib import auth


# Create your models here.
class Media_Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Subject_Name = models.CharField(max_length=80)
    Topic_Name = models.CharField(max_length=80)
    Description = models.CharField(max_length=250)
    Link = models.CharField(max_length=100)

    def __str__(self):
        return self.Topic_Name


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
