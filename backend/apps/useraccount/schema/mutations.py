import graphene
import graphql_jwt
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .types import UserType, UserRoleEnum, GenderEnum
from apps.useraccount.tasks import track_user_login
from utils.ip import get_client_ip

User = get_user_model()


class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        user = info.context.user
        
        if user.is_authenticated:
            ip = get_client_ip(info)
            ua_string = info.context.META.get('HTTP_USER_AGENT', '')
            track_user_login.delay(
                user=user.id, 
                ua_string=ua_string,
                ip_address=ip,
                )

        return cls(user=info.context.user)


class CreateUser(graphene.Mutation):

    class Arguments:
        username = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        gender = graphene.Argument(GenderEnum)
        role = graphene.Argument(UserRoleEnum, required=True)

    user = graphene.Field(UserType)
    created = graphene.Boolean()
    error = graphene.String()

    @staticmethod
    def mutate(root, info, email, first_name, last_name, password, username, gender, role):
        try:
            user = User.objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name,
                username=username,
                role=role.value,
                gender=gender.value,
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