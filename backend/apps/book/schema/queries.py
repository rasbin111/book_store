import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .types import BookType, CategoryType
from .filters import BookFilter
from apps.book.models import Book, Category, BookImage


class BookQuery(graphene.ObjectType):
    books = DjangoFilterConnectionField(BookType, filterset_class=BookFilter)
    # book_by_id = graphene.Field(BookType, id=graphene.ID(required=True))
    book_by_id = graphene.relay.Node.Field(BookType)
    books_by_category = DjangoFilterConnectionField(
        BookType, 
        filterset_class=BookFilter
    )

    # @staticmethod
    # def resolve_book_by_category(root, info, category_slug, **kwargs):
    #     # 2. Your custom logic here
    #     # You can perform complex joins, filtering, or permission checks
    #     queryset = Book.objects.filter(category__slug=category_slug)
        
    #     if not queryset.exists():
    #         return Book.objects.none()
            
    #     return queryset
    # # @staticmethod
    # # def resolve_books(root, info):
    # #     return Book.objects.all()

    # @staticmethod
    # def resolve_book_by_id(root, info, id):
    #     type_name, pk = from_global_id(id)
    #     print("My print: ", type_name, pk)

    #     if type_name == "Boobs":
    #         return Book.objects.get(pk=pk)
    #     return None


class CategoryQuery(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category_by_id = graphene.Field(CategoryType, id=graphene.ID(required=True))

    @staticmethod
    def resolve_categories(root, info):
        return Category.objects.all()

    @staticmethod
    def resolve_category_by_id(root, info, id):
        return Category.objects.get(pk=id)
