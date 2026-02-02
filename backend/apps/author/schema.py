from graphene import List, ObjectType
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import permission_required, login_required

from .models import Author

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ["id", "author_id", "name", "average_reviews", "followers_count"]


class AuthorQuery(ObjectType):
    all_authors = List(AuthorType)

    @staticmethod
    @permission_required("author.view_author")
    def resolve_all_authors(root, info):
        authors = Author.objects.all()
        return authors

