Introduction
------------

Django-unsocial is a Middleware which remove social widgets (ex: the Like button) while developing

Some widgets have a tendency to throw exceptions when a JavaScript console is opened or makes annoying
external requests.

Unsocial is there to address those annoyance.

**Warning**: It is not recommanded to use it in a production environment, it is intended for development use only.

Installation
------------

 1. add *unsocial.middleware.UnsocialMiddleware* to *MIDDLEWARE_CLASSES* your *settings.py*

 2. Set *UNSOCIAL = True* in your *settings.py*


Customizing
-----------

A simple list of regular expressions are used to comment unwanted HTML chunks.
It's possible to override the default list in your *settings.py* like this::

    UNSOCIAL_PATTERNS = [
        r'(<script\s+?.*facebook\.\w+\/.*</script>)',
        r'(<fb:like\s+?.*</fb:like>)',
    ]

Or extend it like this::

    from unsocial.blocklist import PATTERNS

    UNSOCIAL_PATTERNS = PATTERNS + [
        r'(<fb:wall\s+?.*</fb:wall>)',
    ]

Don't hesitate to contribute your patterns !
