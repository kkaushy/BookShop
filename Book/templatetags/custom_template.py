from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def att(h, key):
	return h[str(key)]
	
@register.filter	
def multiply(value, arg):
    return value*arg
    