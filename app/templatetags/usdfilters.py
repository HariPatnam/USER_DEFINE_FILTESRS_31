from django import template

register=template.Library()

def swap(value):
    return value.swapcase()
register.filter('swapping',swap)

def remove(value,arg):
    return value.(arg,'')
register.filter()