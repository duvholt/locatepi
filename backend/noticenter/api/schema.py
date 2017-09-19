from graphene_django import DjangoObjectType
import graphene
from .models import Server as ServerModel, Ping as PingModel


class Server(DjangoObjectType):
    ip = graphene.String(source='ip')

    class Meta:
        model = ServerModel
        only_fields = ('id', 'name',)


class Ping(DjangoObjectType):
    class Meta:
        model = PingModel


class Query(graphene.ObjectType):
    servers = graphene.List(Server)
    pings = graphene.List(Ping)

    def resolve_servers(self, info):
        return ServerModel.objects.all()


schema = graphene.Schema(query=Query)
