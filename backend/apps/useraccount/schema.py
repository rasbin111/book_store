import graphene
from graphene_django import DjangoObjectType
import graphql_jwt
from django.contrib.auth import get_user_model

User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ("password", )


class UserAccountQuery(graphene.ObjectType):
    all_users = graphene.List(UserType)

    @staticmethod
    def resolve_all_users(root, info):
        users = User.objects.all()
        return users


class AuthenticationMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Verify.Field()


class UserAccountMutation(AuthenticationMutation):
    pass
