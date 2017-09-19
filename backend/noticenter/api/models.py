from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=200)


class Ping(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    ip = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
