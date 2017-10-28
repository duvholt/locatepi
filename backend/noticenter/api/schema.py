from graphene_django import DjangoObjectType, DjangoConnectionField
from graphene import relay
import graphene
from .models import Server as ServerModel, Ping as PingModel


class Server(DjangoObjectType):
    ip = graphene.String(source='ip')
    lastUpdate = graphene.String(source='lastUpdate')

    class Meta:
        model = ServerModel
        filter_fields = ['id', 'name']
        only_fields = ['id', 'name']
        interfaces = (relay.Node,)


class Ping(DjangoObjectType):
    class Meta:
        model = PingModel
        filter_fields = ['id']
        interfaces = (relay.Node,)


class CreatePing(graphene.Mutation):
    class Arguments:
        server_name = graphene.String()
        api_key = graphene.String()
        local_ip = graphene.String()

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, server_name, api_key, local_ip):
        ok = False
        server = ServerModel.objects.filter(
            name=server_name, api_key=api_key
        ).first()
        if server:
            PingModel(
                server=server,
                ip=info.context.META['REMOTE_ADDR'],
                local_ip=local_ip,
            ).save()
            ok = True
        return CreatePing(ok=ok)


class Query(graphene.ObjectType):
    servers = DjangoConnectionField(Server)


class MyMutations(graphene.ObjectType):
    create_ping = CreatePing.Field()


schema = graphene.Schema(query=Query, mutation=MyMutations)
