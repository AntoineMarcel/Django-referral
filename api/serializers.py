# serializers.py
from rest_framework import serializers

from .models import Parrain, Campaign

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('message', "background_color", "text_color")

class ParrainSerializer(serializers.ModelSerializer):
    campaign = CampaignSerializer()

    class Meta:
        model = Parrain
        fields = ('campaign',)