from django.db import models

# Create your models here.
from django.db import models
from django.contrib.humanize.templatetags import humanize


# Create your models here.


class CoreModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @property
    def get_created_at(self):
        return humanize.naturaltime(self.created)
