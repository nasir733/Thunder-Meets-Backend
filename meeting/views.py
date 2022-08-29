import uuid

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import    Response
from rest_framework.decorators import action
from meeting.serializers import MeetingSerializer
from meeting.models import Meetings
from .agora_key.RtcTokenBuilder import RtcTokenBuilder, Role_Attendee
import os
import json
import time
from agora_token_builder import RtcTokenBuilder
import random
from rest_framework import permissions
class Meeting(ModelViewSet):
    """
#Sample Post Request Body for creating a meeting
```
    {
   "agendas":[
      {
         "name":"htmasdfdsfl",
         "description":"talk about hrml",
         "time_stamp":"2022-08-28T18:30:09Z"
      }
   ],
   "meeting_name":"Test",
    "channel_name":"Test",
   "meeting_description":"alskdjfldsjkf",
   "meeting_status":true,
   "meeting_timestamp":"2022-08-28T18:33:47Z",
}
```
    """
    serializer_class = MeetingSerializer
    queryset = Meetings.objects.filter(meeting_status=True)
    search_fields = (
        "channel_name",

    )
    def get_permissions(self):
        if self.action == "retrieve" or self.action == "list":
            permission_classes = [permissions.AllowAny]

        elif self.action == "create" or self.action == "generate_agora_token" :
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]


    @action(detail=False)
    def generate_agora_token(self,request):
        print(request.POST)
        appID = os.environ.get('AGORA_APP_ID')
        appCertificate = os.environ.get('AGORA_APP_CERTIFICATE')
        channelName =request.GET.get('channelName')
        print(appID,"app id =============")
        print(appCertificate,"app certificate =============")
        print(channelName,'channelName----')
        SchedulerUser= request.user
        AttendedUser = request.GET.get('AttendedUser')
        expireTimeInSeconds = 3600
        currentTimestamp = int(time.time())
        privilegeExpiredTs = currentTimestamp + expireTimeInSeconds
        uid = random.randint(1, 230)
        expirationTimeInSeconds = 3600
        currentTimeStamp = int(time.time())
        privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
        role = 1

        token = RtcTokenBuilder.buildTokenWithUid(appID, appCertificate, channelName, uid, role, privilegeExpiredTs)
        return Response({'token': token, 'uid': uid})

    @action(detail=False)
    def my_meetings(self,request):
        user = request.user
        if user.is_authenticated:
            meetings = Meetings.objects.filter(meeting_created_by=user)
            serializer = MeetingSerializer(meetings,many=True)
            return Response(serializer.data)

        return Response("User not authenticated",status=401)


class AgoraToken(APIView):
    def get(self,request):
        return Response({"message":"Hello World"})
