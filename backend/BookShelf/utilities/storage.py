from django.core.files.storage import FileSystemStorage
import os
import glob


class ReplaceExistingFileStorage(FileSystemStorage):
    """
    Custom file storage class that deletes the existing file
    from the file system before saving a new one.
    """

    # def get_available_name(self, name, max_length=None):
    #     # If the file already exists, delete it before saving the new one
    #     if self.exists(name):
    #         os.remove(self.path(name))

    #     return super().get_available_name(name, max_length=max_length)
    def get_available_name(self, name, max_length=None):
        # Get the full file path without extension
        base_name, _ = os.path.splitext(self.path(name))

        # Delete any existing file with the same base name,
        # regardless of extension
        # Matches all files with the same name but any extension
        for file_path in glob.glob(f"{base_name}.*"):
            try:
                os.remove(file_path)
            except OSError as e:
                print(f"Error deleting file {file_path}: {e}")

        return super().get_available_name(name, max_length=max_length)
