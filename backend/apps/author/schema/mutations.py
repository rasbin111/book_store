import graphene

from .types import AuthorType
from apps.author.models import Author
from graphql_jwt.decorators import login_required, permission_required


class CreateAuthor(graphene.Mutation):

    class Arguments:
        author_id = graphene.String(required=True)
        name = graphene.String(required=True)
    
    author = graphene.Field(AuthorType)
    created = graphene.Boolean()
    error = graphene.String()

    
    @staticmethod
    @login_required
    @permission_required(["author.add_author"])
    def mutate(root, info, **kwargs):
        try:
            author = Author.objects.create(
                **kwargs
            )
            return CreateAuthor(author=author, created=True, error="")
        except Exception as e:
            return CreateAuthor(author=None, created=False, error=str(e))
        

class AuthorMutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()