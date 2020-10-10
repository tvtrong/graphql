import swapi.schema
import graphene


class Query(swapi.schema.Query,  # Add your Query objects here
            graphene.ObjectType):
    pass


class Mutation(swapi.schema.Mutation,  # Add your Mutation objects here
               graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
