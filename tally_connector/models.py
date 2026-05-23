from django.db import models

# Create your models here.
class TallyServer(models.Model):
    name = models.CharField(max_length=100)

    host = models.CharField(max_length=100, default="localhost")

    port = models.IntegerField(default=9000)

    active = models.BooleanField(default=True)


class TallyXMLLog(models.Model):

    request_xml = models.TextField()

    response_xml = models.TextField()

    request_type = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)