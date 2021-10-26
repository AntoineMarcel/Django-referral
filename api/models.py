from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import date    
from django.conf import settings
import uuid

def RandomID():
    id = uuid.uuid4().hex[:6].upper()
    return id

class Campaign(models.Model):
    token = models.CharField(max_length=6, default=RandomID, unique=True, editable=False)
    background_color = models.CharField(max_length=60)
    text_color = models.CharField(max_length=60)
    message = models.CharField(max_length=200)
    web_site = models.CharField(max_length=200)

    def message_personnalized(self, parrain):
        return self.message.replace("{{firstName}}", parrain.firstName)

class Steps(models.Model):
    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
    )
    order = models.IntegerField()

    class Meta:
        unique_together = ('campaign', 'order',)

class Parrain(models.Model):
    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
    )
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    userCode = models.CharField(max_length=6, default=RandomID, unique=True, editable=False)
    addDate = models.DateField(default=date.today)
    step = models.ForeignKey(
        Steps,
        on_delete=models.CASCADE,
    )
    visits = models.IntegerField(default=0)
    buy = models.IntegerField(default=0)

    def __str__(self):
        return self.firstName

    class Meta:
        unique_together = ('campaign', 'email',)