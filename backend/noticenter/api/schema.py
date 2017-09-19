from graphene_django import DjangoObjectType
import graphene
from .models import Server as ServerModel, Ping as PingModel


class Server(DjangoObjectType):
    class Meta:
        model = ServerModel


class Ping(DjangoObjectType):
    class Meta:
        model = PingModel


class Query(graphene.ObjectType):
    servers = graphene.List(Server)
    pings = graphene.List(Ping)

    @graphene.resolve_only_args
    def resolve_servers(self):
        return ServerModel.objects.all()


schema = graphene.Schema(query=Query)
