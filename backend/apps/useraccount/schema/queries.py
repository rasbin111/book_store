import graphene
from graphql import GraphQLError
from django.contrib.auth import get_user_model
from graphene_django.filter import DjangoFilterConnectionField

from .types import UserType, UserOrderType
from .filters import UserFilter

from apps.useraccount.models import UserOrder


User = get_user_model()


class UserAccountQuery(graphene.ObjectType):
    # all_users = graphene.List(UserType)
    all_users = DjangoFilterConnectionField(UserType, filterset_class=UserFilter)

    user_by_id = graphene.relay.Node.Field(UserType)
    # @staticmethod
    # def resolve_all_users(root, info, **kwargs):
    #     users = User.objects.all()
    #     return users


class UserOrderQuery(graphene.ObjectType):
    user_orders = graphene.List(UserOrderType)

    @staticmethod
    def resolve_user_orders(root, info):
        try:
            user = info.context.user
            if user.is_authenticated:
                orders = UserOrder.objects.filter(user=user)
                return orders
            else:
                raise GraphQLError("You must login to view orders")
        except Exception as e:
            raise GraphQLError(str(e))