"""Module for defining custom decorators."""
import logging
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
logging.basicConfig(level=logging.INFO)


def cache_response(function):
    """Function caching JSON response of GET/POST methods for provided project and resource name"""
    def wrapper(request, *args, **kwargs):
        try:
            cache_key = (request.method,
                         kwargs['project_name'], kwargs['resource_name'])
            if cache_key not in cache:
                logging.info("key %s not found in cache.", cache_key)
                cached_data = function(request, *args, **kwargs)
                cache.set(cache_key, cached_data, timeout=CACHE_TTL)
            return cache.get(cache_key)
        except Exception as cache_error:
            logging.error("%s", cache_error)
    return wrapper
