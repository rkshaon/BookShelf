from django.core.files.storage import FileSystemStorage
import os


class ReplaceExistingFileStorage(FileSystemStorage):
    """
    Custom file storage class that deletes the existing file
    from the file system before saving a new one.
    """

    def get_available_name(self, name, max_length=None):
        # If the file already exists, delete it before saving the new one
        if self.exists(name):
            os.remove(self.path(name))

        return super().get_available_name(name, max_length=max_length)
