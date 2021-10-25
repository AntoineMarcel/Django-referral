from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import date    
from django.conf import settings

class Campaign(models.Model):
    token = models.CharField(max_length=60, default="1234")
    background_color = models.CharField(max_length=60)
    text_color = models.CharField(max_length=60)
    message = models.CharField(max_length=60)

    def message_personnalized(self, parrain):
        return self.message.replace("{{firstName}}", parrain.firstName)

class Steps(models.Model):
    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        blank=True,null=True
    )
    order = models.IntegerField(default=0)

class Parrain(models.Model):
    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        blank=True,null=True
    )
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    userCode = models.CharField(max_length=60)
    addDate = models.DateField(default=date.today)
    step = models.ForeignKey(
        Steps,
        on_delete=models.CASCADE,
        blank=True,null=True
    )
    visits = models.IntegerField(default=0)
    buy = models.IntegerField(default=0)

    def __str__(self):
        return self.firstName