import graphene

from apps.useraccount.schema import UserAccountQuery, UserAccountMutation
from apps.author.schema import AuthorQuery


class Query(AuthorQuery, UserAccountQuery, graphene.ObjectType):
    pass

class Mutation(UserAccountMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
