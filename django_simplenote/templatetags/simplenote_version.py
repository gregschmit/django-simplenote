from django import template
from django_simplenote import version

register = template.Library()


@register.simple_tag
def get_version():
    print(version.get_version())
    return version.get_version()
