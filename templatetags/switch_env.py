from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def switch_env(value):
    return value.replace("104.196.27.12", "statehouses-api.gannettdigital.com")
