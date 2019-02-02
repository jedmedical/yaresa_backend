
from django import template

register = template.Library()

@register.filter(name='is_superman')
def is_superman(user):

    return True if user.is_superuser else False
