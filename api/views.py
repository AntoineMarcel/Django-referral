from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ParrainSerializer
from .models import Parrain

class Parrains(APIView):
    def get(self, request, campaignToken=None, userCode=None):
        if userCode and campaignToken:
            try:
                item = Parrain.objects.get(userCode=userCode)
                if not item.campaign.token == campaignToken:
                    return Response({"status": "error"})
            except:
                return Response({"status": "error"})
            serializer = ParrainSerializer(item)
            item.visits = item.visits + 1
            item.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error"})