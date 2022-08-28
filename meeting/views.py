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
   "meeting_location":"Wah",
   "meeting_description":"alskdjfldsjkf",
   "meeting_status":true,
   "meeting_timestamp":"2022-08-28T18:33:47Z",
   "meeting_created_at":"2022-08-28T18:34:08.312519Z",
   "meeting_updated_at":"2022-08-28T18:34:08.312538Z",
}
```
    """
    serializer_class = MeetingSerializer
    queryset = Meetings.objects.all()


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
        if channelName:

            token = RtcTokenBuilder.buildTokenWithAccount(
            appID, appCertificate, channelName, SchedulerUser, Role_Attendee, privilegeExpiredTs)

            return Response({'token': token, 'appID': appID})
        else:
            return Response({'error': 'channelName is required'})







class AgoraToken(APIView):
    def get(self,request):
        return Response({"message":"Hello World"})
