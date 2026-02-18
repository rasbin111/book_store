from graphene_django import DjangoObjectType


from apps.author.models import Author


class AuthorType(DjangoObjectType):

    class Meta:
        model = Author
        fields = [
            "id",
            "author_id",
            "name",
            "average_reviews",
            "followers_count"
        ]