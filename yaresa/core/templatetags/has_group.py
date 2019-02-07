from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    users_in_group = Group.objects.get(name=group_name).user_set.all()

    return True if user in users_in_group else False