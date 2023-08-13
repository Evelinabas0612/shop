from django import template

register = template.Library()


@register.filter
def mediapath(photo: str):
    return f'/media/{photo}'


@register.simple_tag
def mediapath(photo: str):
    return f'/media/{photo}'