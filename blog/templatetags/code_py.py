# -*- coding: utf8 -*-
import re 
import pygments 
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from pygments import lexers 
from pygments import formatters 
 
register = template.Library() 
regex = re.compile(r'<code(.*?)>(.*?)</code>', re.DOTALL) 
 
@register.filter(is_safe=True)
@stringfilter
def code_py(value): 
    last_end = 0 
    to_return = '' 
    found = 0 
    for match_obj in regex.finditer(value): 
        code_class = match_obj.group(1) 
        code_string = match_obj.group(2) 
        if code_class.find('class'): 
            language = re.split(r'"|\'', code_class)[1] 
            lexer = lexers.get_lexer_by_name(language) 
        else: 
            try: 
                lexer = lexers.guess_lexer(str(code_string)) 
            except ValueError: 
                lexer = lexers.PythonLexer() 
        pygmented_string = pygments.highlight(code_string, lexer, formatters.HtmlFormatter()) 
        to_return = to_return + value[last_end:match_obj.start(0)] + pygmented_string 
        last_end = match_obj.end(2) 
        found = found + 1 
    to_return = to_return + value[last_end:] 
    return to_return 