from __future__ import unicode_literals

import warnings

from django import get_version as get_django_version

# Much like registering signal handlers. We import this module so that its registrations get picked up
# the NO QA directive tells flake8 to not complain about the unused import
from . import event_handlers  # NOQA

__title__ = "dj-stripe"
__summary__ = "Django + Stripe Made Easy"
__uri__ = "https://github.com/pydanny/dj-stripe/"

__version__ = "0.8.0"

__author__ = "Daniel Greenfeld"
__email__ = "pydanny@gmail.com"

__license__ = "BSD"
__license__ = "License :: OSI Approved :: BSD License"
__copyright__ = "Copyright 2015 Daniel Greenfeld"

if get_django_version() <= "1.7.x":
    msg = (
        "dj-stripe deprecation notice: Django 1.7 and lower are no longer\n"
        "supported. Please upgrade to Django 1.8 or higher.\n"
        "Reference: https://github.com/pydanny/dj-stripe/issues/275"
    )
    warnings.warn(msg)
