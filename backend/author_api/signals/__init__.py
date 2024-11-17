from author_api.signals.cache import clear_author_cache_on_save
from author_api.signals.cache import clear_author_cache_on_delete


__all__ = [
    clear_author_cache_on_save,
    clear_author_cache_on_delete,
]
