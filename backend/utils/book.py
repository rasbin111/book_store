from datetime import datetime
from django.utils.text import slugify
def book_image_directory_path(instance, filename):  # pylint: disable = unused-argument
    """Upload path to save file"""
    book_instance = instance.book.title or "book"
    book = slugify(book_instance)
    
    return f"books/{book}/{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}_{filename}"