import graphene
from graphql import GraphQLError

from apps.order.models import UserOrder
from .types import UserAddressType, UserOrderType


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