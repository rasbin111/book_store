import graphene

from .types import BookType
from apps.book.models import Book
from graphql_jwt.decorators import login_required


class BookQuery(graphene.ObjectType):
    books = graphene.List(BookType)

    @staticmethod
    def resolve_books(root, info):
        return Book.objects.all()