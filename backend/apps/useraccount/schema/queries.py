import graphene
from django.contrib.auth import get_user_model
from graphene_django.filter import DjangoFilterConnectionField

from .types import UserType
from .filters import UserFilter

User = get_user_model()


class UserAccountQuery(graphene.ObjectType):
    # all_users = graphene.List(UserType)
    all_users = DjangoFilterConnectionField(UserType, filterset_class=UserFilter)

    user_by_id = graphene.relay.Node.Field(UserType)
    # @staticmethod
    # def resolve_all_users(root, info, **kwargs):
    #     users = User.objects.all()
    #     return users



