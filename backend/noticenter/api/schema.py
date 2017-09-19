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


class CreatePing(graphene.Mutation):
    class Arguments:
        server_name = graphene.String()
        api_key = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, server_name, api_key):
        ok = False
        server = ServerModel.objects.filter(
            name=server_name, api_key=api_key
        ).first()
        if server:
            PingModel(server=server, ip=info.context.META['REMOTE_ADDR']).save()
            ok = True
        return CreatePing(ok=ok)


class Query(graphene.ObjectType):
    servers = graphene.List(Server)
    pings = graphene.List(Ping)

    def resolve_servers(self, info):
        return ServerModel.objects.all()


class MyMutations(graphene.ObjectType):
    create_ping = CreatePing.Field()


schema = graphene.Schema(query=Query, mutation=MyMutations)
