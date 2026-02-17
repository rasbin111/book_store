import graphene
from graphql import GraphQLError

from graphene_django import DjangoObjectType
import graphql_jwt
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

class UserRoleEnum(graphene.Enum):
    SUPER_USER = "superuser"
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

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

class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)


class CreateUser(graphene.Mutation):

    class Arguments:
        username = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        role = graphene.Argument(UserRoleEnum, required=True)

    user = graphene.Field(UserType)
    created = graphene.Boolean()
    error = graphene.String()

    @staticmethod
    def mutate(root, info, email, first_name, last_name, password, username, role):
        try:
            user = User.objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name,
                username=username,
                role=role.value
            )
            user.set_password(password)

            group = Group.objects.get(name=role.value)
            
            if not group:
                group = Group.objects.get_or_create(name="viewer")
                

            user.groups.set([group])
            user.save()
            return CreateUser(user=user, created=True, error="") 
        except Exception as e:
            return CreateUser(user=None, created=False, error=str(e)) 
            

class AuthenticationMutation(graphene.ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Verify.Field()


class UserAccountMutation(AuthenticationMutation):
    create_user = CreateUser.Field()
