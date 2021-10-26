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
                    return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
            serializer = ParrainSerializer(item)
            item.visits = item.visits + 1
            item.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

class CreateParrains(APIView):
    def post(self, request):
        try:
            campaign = Campaign.objects.get(token=request.data['campaignTk'])
            if not request.META['HTTP_HOST'] in campaign.site:
                return Response({"status": "error", "data": {"error" : "not the good domain"}}, status=status.HTTP_400_BAD_REQUEST)
            parrain = {
                'campaign':campaign.id,
                'firstName': request.data['firstName'],
                'lastName': request.data['lastName'],
                'email': request.data['email'],
                'step': Steps.objects.get(campaign=campaign, order=0).id,
            }
            serializer = CreateParrainSerializer(data=parrain)
            if serializer.is_valid():
                serializer.save()
                if request.data['userCode']:
                    try:
                        fromUser = Parrain.objects.get(userCode=request.data['userCode'])
                        if fromUser.campaign.token == request.data['campaignTk']:
                            fromUser.buy = fromUser.buy + 1
                            fromUser.save()
                    except:
                        pass
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            data = {
                "except" : str(e),
                "data" : request.data
            }
            return Response({"status": "error", "data": data}, status=status.HTTP_400_BAD_REQUEST)