from django import template

register = template.Library()

@register.filter(name='cut_word')
def cut_word(value, arg):
    """
    This cuts out all values of arg from string
    """
    return value.replace(arg, '')

# register.filter('cut_word', cut_word)
