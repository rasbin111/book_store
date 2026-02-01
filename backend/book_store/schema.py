import graphene

from apps.useraccount.schema import UserAccountQuery, UserAccountMutation


class Query(UserAccountQuery, graphene.ObjectType):
    pass

class Mutation(UserAccountMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)