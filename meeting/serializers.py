from rest_framework.serializers import ModelSerializer
from .models import Meetings,Agendas

class AgendasSerializer(ModelSerializer):
    class Meta:
        model = Agendas
        fields = '__all__'
class MeetingSerializer(ModelSerializer):
    agendas = AgendasSerializer(many=True)
    class Meta:
        model = Meetings
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        print(user)
        agendas_data = validated_data.pop('agendas')
        meeting = Meetings.objects.create(**validated_data,meeting_created_by=user)
        for agenda_data in agendas_data:
            agenda = Agendas.objects.create(meeting=meeting,**agenda_data)





        return meeting