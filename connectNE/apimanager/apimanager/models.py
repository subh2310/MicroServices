from django.db import models

# Create your models here.
class ConnectNE(models.Model):
    handle = models.CharField(max_length=100, default=None)
    username = models.CharField(max_length=100, default = "temp")
    password = models.CharField(max_length=100, default="root")
    hostname = models.CharField(max_length=100, default=None)
    port_number = models.IntegerField(default=22)
    interface = models.CharField(max_length=50, default="CLI")