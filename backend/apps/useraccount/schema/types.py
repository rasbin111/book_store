import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from apps.order.schema import UserOrderType, UserAddressType

User = get_user_model()


class UserRoleEnum(graphene.Enum):
    SUPER_USER = "superuser"
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"


class GenderEnum(graphene.Enum):
    MALE = 0
    FEMALE = 1
    OTHER = 2


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ("password", )
        interfaces = (graphene.relay.Node, )
    
    user_orders = graphene.List(lambda: UserOrderType)
    address = graphene.Field(lambda: UserAddressType)
    gender = graphene.Field(GenderEnum)
