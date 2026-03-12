from graphene_django import DjangoObjectType

from apps.order.models import UserOrder, UserAddress

class UserOrderType(DjangoObjectType):

    class Meta:
        model = UserOrder
        fields = [
            "order_id",
            "address",
            "payment_status",
            "order_amount",
            "tax",
            "delivery_charge",
            "total_amount",
            "paid_amount",
            "delivery_person",
            "expected_delivery_date",
        ]

class UserAddressType(DjangoObjectType):

    class Meta:
        model = UserAddress
        fields = [
            "id",
            "address_type",
            "country",
            "city",
            "street",
            "postal_code",
            "phone_number",
            "alt_phone_number",
        ]
