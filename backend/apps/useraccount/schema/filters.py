import django_filters
from django.contrib.auth import get_user_model

from utils.constants import USER_ROLES_CHOICES, GENDER_CHOICES

User = get_user_model()


class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter("name", lookup_expr="icontains")
    email = django_filters.CharFilter("email", lookup_expr="icontains")
    username = django_filters.CharFilter("username", lookup_expr="icontains")
    role = django_filters.ChoiceFilter("role", choices=USER_ROLES_CHOICES)
    gender = django_filters.ChoiceFilter("gender", choices=GENDER_CHOICES)

    class Meta:
        model = User
        fields = []

    order_by = django_filters.OrderingFilter(
        fields=(
            "created_at",
            "updated_at",
        )
    )