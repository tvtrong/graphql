import graphene


class DHT11Type(graphene.ObjectType):
    id = graphene.NonNull(graphene.Int)
    timestamp = graphene.NonNull(graphene.DateTime)
    temperature = graphene.NonNull(graphene.Float)
    humidity = graphene.NonNull(graphene.Float)
