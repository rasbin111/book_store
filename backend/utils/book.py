from datetime import datetime

def book_image_directory_path(instance, filename):  # pylint: disable = unused-argument
    """Upload path to save file"""
    book_instance = instance.book.name or "book"
    return f"books/{book_instance}/{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}_{filename}"