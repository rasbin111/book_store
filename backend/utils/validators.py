from django.core.validators import RegexValidator

PHONE_REGEX = RegexValidator(
    regex=r"^\+?\d{7,15}$",
    message="Phone number must be entered in the format: +9779899888888, and upt to 15 digits allowed",
)