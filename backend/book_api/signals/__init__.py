# book_api/signals/__init__.py
from book_api.signals.book_delete import delete_book_files


__all__ = [
    delete_book_files,
]
