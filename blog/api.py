from tastypie.resources import ModelResource
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.authentication import BasicAuthentication, Authentication

from django.contrib.auth.models import User
from tastypie import fields
from blog.models import Post, Comment
from django.db import models
from tastypie.models import create_api_key
__author__ = 'admin'
models.signals.post_save.connect(create_api_key, sender=User)
class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
        
class PostResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = Post.objects.all().order_by("-created")
        resource_name = 'post'
        authentication = Authentication()
        authorization = Authorization()
        
class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        authentication = Authentication()
        authorization = Authorization()        