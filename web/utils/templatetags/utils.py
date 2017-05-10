from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='range')
def filter_range(start, end):
    return range(start, end)


@register.simple_tag
def vue_variable(variable):
    return ("{{" + variable + "}}")


@register.filter(name='greater')
def greater(list, num_elements):
    return len(list) > num_elements


@register.simple_tag
def frontend(path):
    """
    Creates a path pointing to the front end resources.
    """
    return "{0}{1}".format(settings.FRONTEND_URL, path)
