from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cut out all vauels of arg
    """

    return value.replace(arg, '')

# register.filter('cut', cut)
