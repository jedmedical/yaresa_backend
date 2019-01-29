
from django import template

register = template.Library()

@register.filter(name='is_super')
def is_super(user):

    return True if user.is_superuser else False
