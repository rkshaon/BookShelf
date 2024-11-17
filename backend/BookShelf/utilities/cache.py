# from django.utils.cache import _generate_cache_key, get_cache_key
from django.core.cache import cache
# from django.http import HttpRequest
from hashlib import md5


# def invalidate_author_cache():
#     # cache_key = f"views.decorators.cache.cache_page.{hash('/author/v1/')}"
#     # cache.delete(cache_key)
#     request = HttpRequest()
#     request.method = "GET"
#     request.path = "/author/v1/"
#     # request.META = {"HTTP_ACCEPT_LANGUAGE": "en-us"}  # Match locale if set
#     request.META = {
#         "HTTP_ACCEPT_LANGUAGE": "en-us",  # Ensure locale matches
#         "SERVER_NAME": "127.0.0.1",       # Add server name
#         "SERVER_PORT": "8001",            # Add server port
#     }
#     # cache_key = _generate_cache_key(request)
#     # print(f"Invalidating Cache Key: {cache_key}")  # For debugging
#     # cache.delete(cache_key)

#     cache_key = get_cache_key(request)

#     if cache_key:
#         print(f"Invalidating Cache Key: {cache_key}")  # Debugging
#         cache.delete(cache_key)
#     else:
#         print("Cache key not found for the given request")


def generate_cache_key(path):
    # Hash the path to match the stored pattern
    hashed_path = md5(path.encode('utf-8')).hexdigest()
    # Replace 'en-us.UTC' if your locale/timezone differs
    key = f":1:views.decorators.cache.cache_page..GET.{hashed_path}.en-us.UTC"
    return key


def invalidate_author_cache():
    path = "/author/v1/"
    cache_key = generate_cache_key(path)
    print(f"Invalidating Cache Key: {cache_key}")
    if cache.delete(cache_key):
        print("Cache key invalidated successfully")
    else:
        print("No matching cache key found")
