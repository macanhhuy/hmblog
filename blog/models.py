from django.db import models
from django.db.models import permalink
from django.conf.locale import sl
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import os
from filebrowser.fields import FileBrowseField
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

  

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Category(models.Model):
    title = models.CharField(max_length=80)
    slug = models.CharField(max_length=100,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    position = models.PositiveSmallIntegerField("Position")
    class Meta:
        ordering = ['position']
    def save(self, *args, **kwargs):
        if self.slug != "":
            super(Category, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.title)            
            super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
    @permalink
    def get_absolute_url(self):
        return "/category/%s/" % self.slug   
class TaggedPost(TaggedItemBase):
    content_object = models.ForeignKey('Post')  
      
class Post(models.Model):
    title = models.CharField(max_length=80)
    slug = models.CharField(max_length=100,blank=True)
    thumbnail = FileBrowseField("Image", max_length=200, blank=True, null=True)
    user = models.ForeignKey(User)
    category = models.ManyToManyField(Category)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(through=TaggedPost)
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains","category__icontains")
    def save(self, *args, **kwargs):
                            
        if self.slug != "":
            super(Post, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.title)            
            super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
    @permalink
    def get_absolute_url(self):
        return "/%s.html" % self.slug 

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)
    def __unicode__(self):
        return u"%s: %s" % (self.post, self.body[:60])  
    
class Image(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image = FileBrowseField("Image", max_length=200, blank=True, null=True)
    position = models.PositiveSmallIntegerField("Position")
    post = models.ForeignKey(Post)
    class Meta:
        ordering = ['position']
    def __unicode__(self):
        return u"%s" % (self.image)  