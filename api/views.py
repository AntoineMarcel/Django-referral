from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ParrainSerializer, CreateParrainSerializer
from .models import Parrain, Campaign, Steps

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

class CreateParrains(APIView):
    def post(self, request):
        try:
            campaign = Campaign.objects.get(token=request.data['campaignTk'])
            if not request.GET._mutable:
                request.data._mutable = True
            request.data['campaign'] = campaign.id
            request.data['step'] = Steps.objects.get(campaign=campaign, order=0).id
            request.data.pop('campaignTk')
            serializer = CreateParrainSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            data = {
                "except" : str(e),
                "data" : request.data
            }
            return Response({"status": "error", "data": data})