import django_filters

from apps.book.models import Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter("title", lookup_expr="icontains")

    price_min = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    
    class Meta:
        model = Book
        fields = ["title", "price"]

    order_by = django_filters.OrderingFilter(fields=(
        "created_at",
        "updated_at"
    ))