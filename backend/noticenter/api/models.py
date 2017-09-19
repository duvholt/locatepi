from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=200)

    @property
    def ip(self):
        latest_ping = self.pings.order_by('-time').first()
        if latest_ping:
            return latest_ping.ip
        return None


class Ping(models.Model):
    server = models.ForeignKey(Server, related_name='pings', on_delete=models.CASCADE)
    ip = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
