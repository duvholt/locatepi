from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=200)

    @property
    def ip(self):
        latest_ping = self._latest_ping()
        if latest_ping:
            return latest_ping.ip
        return None

    @property
    def lastUpdate(self):
        latest_ping = self._latest_ping()
        if latest_ping:
            return latest_ping.time
        return None

    def _latest_ping(self):
        return self.pings.order_by('-time').first()

    def __str__(self):
        return self.name


class Ping(models.Model):
    server = models.ForeignKey(Server, related_name='pings', on_delete=models.CASCADE)
    ip = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        timestamp = self.time.strftime('%Y-%m-%d %H:%M:%S')
        return f'Ping from {self.server}({self.ip}) at {timestamp}'
