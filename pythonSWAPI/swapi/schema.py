import graphene
from .types import DHT11Type
from .resolvers import resolver_dht11s, resolver_dht11est, resolver_create_dht11, resolver_update_dht11, resolver_delete_dht11
from django.db.models import Q
# truy vấn gốc


class Query(graphene.ObjectType):
    dht11s = graphene.List(DHT11Type,
                           first=graphene.Int(),
                           skip=graphene.Int(), )

    def resolve_dht11s(self, info, first, skip):
        dht11s = resolver_dht11s()
        if skip:
            dht11s = dht11s[skip:]
        if first:
            dht11s = dht11s[:first]
        return dht11s

    dht11est = graphene.Field(DHT11Type)

    def resolve_dht11est(self, info):
        return resolver_dht11est()


class Mutation(graphene.ObjectType):
    # Quá trình gửi dữ liệu đến máy chủ được gọi là quá trình đột biến
    create_dht11 = graphene.Field(DHT11Type,
                                  temperature=graphene.NonNull(graphene.Float),
                                  humidity=graphene.NonNull(graphene.Float))

    def resolve_create_dht11(self, info, temperature, humidity):
        return resolver_create_dht11(temperature, humidity)

    update_dht11 = graphene.Field(DHT11Type,
                                  id=graphene.NonNull(graphene.Int),
                                  timestamp=graphene.NonNull(
                                      graphene.DateTime),
                                  temperature=graphene.NonNull(graphene.Float),
                                  humidity=graphene.NonNull(graphene.Float))

    def resolve_update_dht11(self, info, id, timestamp, temperature, humidity):
        if info.context.user.is_anonymous:
            raise Exception('You are not authenticated!')
        return resolver_update_dht11(id, timestamp, temperature, humidity)

    delete_dht11 = graphene.Field(graphene.NonNull(graphene.String),
                                  id=graphene.NonNull(graphene.Int))

    def resolve_delete_dht11(self, info, id):
        resolver_delete_dht11(id=id)
        return "Deleted successfully !"


# xuất Lược đồ GraphQL
schema = graphene.Schema(query=Query, mutation=Mutation)
