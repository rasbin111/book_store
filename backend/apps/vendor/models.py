from django.db import models

from apps.core.models import CommonModel
from utils.validators import PHONE_REGEX
from utils.vendor import vendor_file_directory_path


class Vendor(CommonModel):
    name = models.CharField(max_length=255)
    registration_num = models.CharField(max_length=100, unique=True)
    registration_doc = models.FileField(upload_to=vendor_file_directory_path, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, validators=[PHONE_REGEX,])
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    vendor_type = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name