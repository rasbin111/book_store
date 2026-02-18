import graphene
from graphql_jwt.decorators import login_required
from .types import BookType
from apps.book.models import Book, Category
from apps.author.models import Author
from apps.core.models import Language
from graphql_jwt.decorators import permission_required

class CreateBookMutation(graphene.Mutation):

    class Arguments:
        title = graphene.String(required=True)
        category = graphene.Int(required=True)
        authors = graphene.List(graphene.Int, required=True)
        price = graphene.Float(required=True)
        language = graphene.Int()
    
    book = graphene.Field(BookType)
    created = graphene.Boolean()
    error = graphene.String()


    @staticmethod
    @login_required
    @permission_required(["book.create_book"])
    def mutate(root, info, **kwargs):
        try:
            user = info.context.user
            category_id = kwargs.get("category")
            authors_id = kwargs.get("authors")
            authors = Author.objects.filter(id__in=authors_id)
            language_id = kwargs.get("language")
            
            if language_id:
                language = Language.objects.get(id=language_id)
            else:
                """ Default language: English"""
                language = Language.objects.get(name__iexact="English")
            
            kwargs["category"] = Category.objects.get(id=category_id)
            kwargs["language"] = language

            del kwargs["authors"]
            kwargs["added_by"] = user 

            book = Book.objects.create(**kwargs)

            book.authors.set(authors)


            book.save()
            
            return CreateBookMutation(book=book, created=True, error="")
 
        except Exception as e:
            return CreateBookMutation(book=None, created=False, error=str(e))




class BookMutation(graphene.ObjectType):
    create_book = CreateBookMutation.Field()