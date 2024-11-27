# book_api/signals/__init__.py
from book_api.signals.book_delete import delete_book_files
from book_api.signals.book_create import update_book_page_count


__all__ = [
    delete_book_files,
    update_book_page_count,
]
