from django.core.files.storage import FileSystemStorage
import os
import glob


class ReplaceExistingFileStorage(FileSystemStorage):
    """
    Custom file storage class that deletes the existing file
    from the file system before saving a new one.
    """
    def get_available_name(self, name, max_length=None):
        base_name, _ = os.path.splitext(self.path(name))

        for file_path in glob.glob(f"{base_name}.*"):
            try:
                os.remove(file_path)
            except OSError as e:
                print(f"Error deleting file {file_path}: {e}")

        return super().get_available_name(name, max_length=max_length)
