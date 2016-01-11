# -*- coding: utf8 -*-
import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def code_markdown(value):
    return mark_safe(markdown.markdown(value,
        extensions = ['markdown.extensions.extra', 'markdown.extensions.codehilite'],
                                       safe_mode=False,
                                       enable_attributes=False))

