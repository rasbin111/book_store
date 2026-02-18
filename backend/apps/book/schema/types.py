import graphene
from graphene_django import DjangoObjectType

from apps.book.models import Book, Category, BookImage
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
            "images",
            "primary_image",
            "added_by"
        ]

    images = graphene.List(lambda: BookImageType)
    primary_image = graphene.Field(lambda: BookImageType)


    @staticmethod
    def resolve_images(root, info):
        return root.images.all()

    @staticmethod
    def resolve_primary_image(root, info):
        return root.images.filter(is_primary=True).first()
    
class BookImageType(DjangoObjectType):
   
    class Meta:
        model = BookImage
        fields = [
            "id",
            "is_primary",
            "image_file"
        ]
    # language = graphene.Field(lambda: LanguageType)
    # author = graphene.Field(lambda: AuthorType)
    # added_by = graphene.String()

    # @staticmethod
    # def resolve_language(root, info):
    #     print(root)
    #     return root.language
