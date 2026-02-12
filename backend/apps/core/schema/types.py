from graphene_django import DjangoObjectType

from apps.core.models import Language


class LanguageType(DjangoObjectType):

    class Meta:
        model = Language
        field = [
            "id",
            "name"
        ]