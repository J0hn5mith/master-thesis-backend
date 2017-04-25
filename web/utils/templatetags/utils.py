from django import template

register = template.Library()

@register.filter(name='range')
def filter_range(start, end):
  return range(start, end)

@register.simple_tag
def vue_variable(variable):
    return("{{" + variable + "}}")

@register.filter(name='greater')
def greater(list, num_elements):
    return len(list) > num_elements
