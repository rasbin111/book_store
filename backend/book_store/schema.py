import graphene

from apps.useraccount.schema import UserAccountQuery, UserAccountMutation
from apps.author.schema import AuthorQuery
from apps.book.schema.queries import BookQuery

class Query(AuthorQuery, BookQuery,  UserAccountQuery, graphene.ObjectType):
    pass

class Mutation(UserAccountMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
