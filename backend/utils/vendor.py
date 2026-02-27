from datetime import datetime

def vendor_file_directory_path(instance, filename):  # pylint: disable = unused-argument
    """Upload path to save file"""
    return f"vendors/{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}_{filename}"