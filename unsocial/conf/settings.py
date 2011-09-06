from django.conf import settings
from unsocial.blocklist import PATTERNS

UNSOCIAL = getattr(settings, 'UNSOCIAL', False)

UNSOCIAL_PATTERNS = getattr(settings, 'UNSOCIAL_PATTERNS', PATTERNS)

