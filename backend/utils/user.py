from django.utils.text import slugify
from datetime import datetime


def get_unique_username(model_instance, full_name, slug_field_name):
    """
    Takes a model instance, sluggable field name (such as 'title') of that
    model as string, slug field name (such as 'slug') of the model as string;
    returns a unique slug as string.
    """
    # pylint: disable = protected-access
    slug = slugify(full_name)
    unique_slug = slug
    extension = 1
    model_class = model_instance.__class__

    while model_class._default_manager.filter(
        **{slug_field_name: unique_slug}
    ).exists():
        unique_slug = f"{slug}-{extension}"
        extension += 1
    return unique_slug

def user_avatar_directory_path(instance, filename):  # pylint: disable = unused-argument
    """Upload path to save file"""
    return f"user_account/{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}_{filename}"