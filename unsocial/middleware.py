import re
from unsocial.conf import settings


class UnsocialMiddleware(object):

    def __init__(self):
        if not settings.UNSOCIAL:
            from django.core.exceptions import MiddlewareNotUsed
            raise MiddlewareNotUsed


    def process_response(self, request, response):
        if response.status_code != 200 or \
                'html' not in response.get('Content-Type', '').lower():
            return response

        for pattern in settings.UNSOCIAL_PATTERNS:
            response.content = re.sub(pattern, r'<!-- \1 -->', response.content)

        return response

