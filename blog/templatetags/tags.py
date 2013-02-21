from django import template
from blog.models import *
from django.shortcuts import render_to_response
from django.template import Context
from django.http import HttpResponse
from django.conf import settings
from captcha.fields import ReCaptchaField

register = template.Library()

@register.simple_tag
def navactive(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return "active"
    return ""

@register.tag(name="show_category")
def get_categories(request):
    categories = Category.objects.all().order_by("title")
    return categories

@register.simple_tag
def recaptcha_html():
    captcha = ReCaptchaField()  
    return captcha.displayhtml(settings.RECAPTCHA_PUBLIC_KEY)
