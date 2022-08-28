from django.db import models





# Create your models here.
class Meetings(models.Model):
    meeting_name = models.CharField(max_length=100)
    channel_name = models.CharField(max_length=100,unique=True)
    meeting_description = models.TextField()
    meeting_status = models.BooleanField(default=True)
    meeting_timestamp= models.DateTimeField(auto_now_add=False,null=True,blank=True)
    meeting_created_at = models.DateTimeField(auto_now_add=True)
    meeting_updated_at = models.DateTimeField(auto_now=True)
    meeting_created_by = models.ForeignKey('users.User', on_delete=models.CASCADE,null=True,blank=True)




    def __str__(self):
        return self.meeting_name

class Agendas(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    time_stamp = models.DateTimeField(null=True,blank=True)
    meeting = models.ForeignKey(Meetings,on_delete=models.CASCADE,related_name='agendas',null=True,blank=True)


