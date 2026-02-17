import graphene
from graphene_django import DjangoObjectType

from apps.book.models import Book, Category
from apps.author.schema import AuthorType
from apps.core.schema import LanguageType

class CategoryType(DjangoObjectType):

    class Meta:
        model = Category
        fields = ["id", "name"]

class BookType(DjangoObjectType):

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "category",
            "authors",
            "price",
            "review_stars",
            "upload_date",
            "language",
            "added_by"
        ]

    # language = graphene.Field(lambda: LanguageType)
    # author = graphene.Field(lambda: AuthorType)
    # added_by = graphene.String()

    # @staticmethod
    # def resolve_language(root, info):
    #     print(root)
    #     return root.language
