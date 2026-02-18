import graphene

from .types import BookType, CategoryType
from apps.book.models import Book, Category


class BookQuery(graphene.ObjectType):
    books = graphene.List(BookType)
    book_by_id = graphene.Field(BookType, id=graphene.ID(required=True))

    @staticmethod
    def resolve_books(root, info):
        return Book.objects.all()

    @staticmethod
    def resolve_book_by_id(root, info, id):
        return Book.objects.get(pk=id)


class CategoryQuery(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category_by_id = graphene.Field(CategoryType, id=graphene.ID(required=True))

    @staticmethod
    def resolve_categories(root, info):
        return Category.objects.all()

    @staticmethod
    def resolve_category_by_id(root, info, id):
        return Category.objects.get(pk=id)