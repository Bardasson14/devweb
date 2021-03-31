from django import template

register = template.Library()

@register.simple_tag 
def x10(value):
    return value * 10