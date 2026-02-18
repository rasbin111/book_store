import graphene

from apps.useraccount.schema import UserAccountQuery, UserAccountMutation
from apps.author.schema import AuthorQuery, AuthorMutation
from apps.book.schema import BookQuery, BookMutation


class Query(AuthorQuery, BookQuery, UserAccountQuery, graphene.ObjectType):
    pass


class Mutation(AuthorMutation, UserAccountMutation, BookMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
