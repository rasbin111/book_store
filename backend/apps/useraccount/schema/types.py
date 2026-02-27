import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

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