import django_filters

from apps.book.models import Book, Category


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter("title", lookup_expr="icontains")

    price_min = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    category_slug = django_filters.CharFilter(field_name="category__slug", lookup_expr="iexact")
    
    class Meta:
        model = Book
        fields = []

    order_by = django_filters.OrderingFilter(fields=(
        "created_at",
        "updated_at",
        "price",
        "title"
    ))
