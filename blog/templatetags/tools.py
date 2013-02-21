from datetime import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from blog.models import Category
from django import template

register = template.Library()

@register.filter(name='inthuong')
def inthuong(value): # Only one argument.
    """Converts a string into all lowercase value|inthuong"""
    return value.lower()

@register.filter(is_safe=True)
def myfilter(value):
    return value

@register.inclusion_tag("category_list.html", takes_context=True)
def nav_categorylist(context):
        categories = Category.objects.all()
        return {'categories': categories}    
