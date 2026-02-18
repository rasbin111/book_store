import graphene

from .types import AuthorType
from apps.author.models import Author


class Authors(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    author_by_id = graphene.Field(AuthorType, id=graphene.ID(required=True))

    @staticmethod
    def resolve_authors(root, info):
        authors = Author.objects.all()
        return authors

    @staticmethod
    def resolve_author_by_id(root, info, id):
        return Author.objects.get(pk=id)


class AuthorQuery(Authors):
    pass