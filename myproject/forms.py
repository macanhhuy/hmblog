from quix.django.contact.forms import ContactForm
from django.contrib.comments import CommentForm
from captcha.fields import ReCaptchaField

class ReCaptchaContactForm(ContactForm):
    captcha = ReCaptchaField()
    
class ReCaptchaCommentForm(CommentForm):
    captcha = ReCaptchaField()    