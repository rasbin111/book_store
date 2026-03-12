import graphene

from apps.useraccount.schema import UserAccountQuery, UserAccountMutation
from apps.author.schema import AuthorQuery, AuthorMutation
from apps.book.schema import BookQuery, CategoryQuery, BookMutation
from apps.order.schema import UserOrderQuery

class Query(AuthorQuery, BookQuery, CategoryQuery, UserOrderQuery, UserAccountQuery, graphene.ObjectType):
    pass


class Mutation(AuthorMutation, UserAccountMutation, BookMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
