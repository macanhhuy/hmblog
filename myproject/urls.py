from django.conf.urls import patterns, include, url
from filebrowser.sites import site
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from blog.sitemap import *
from tastypie.api import Api
from blog.api import PostResource, UserResource, CommentResource
from todo.api import TodoResoure

sitemaps = {
    "blog": BlogSitemap
}    
admin.autodiscover()
entry_resource = PostResource()
todo_resource = TodoResoure()
cm = CommentResource()
v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(PostResource())

urlpatterns = patterns('home.views',
       (r'^$', 'main'),
       
        )
urlpatterns += patterns('blog.views',
      (r'^blog$', 'main'),
      
        (r"^add_comment/(\d+)/$", "add_comment"),
        (r"^month/(\d+)/(\d+)/$", "month"),
        (r"^delete_comment/(\d+)/$", "delete_comment"),
        (r"^delete_comment/(\d+)/(\d+)/$", "delete_comment"),
        (r'^([\w-]+).html$', 'post'),
        (r'^tag/([\w-]+)$', 'tag'),
         (r'^category/([\w-]+)$', 'category'),
       (r'^demo/', 'demo'),
        )

urlpatterns += patterns('page.views',
        (r'^page$', 'main'),
        (r"^page/add_comment/(\d+)/$", "add_comment"),
        (r"^page/month/(\d+)/(\d+)/$", "month"),
        (r"^page/delete_comment/(\d+)/$", "delete_comment"),
        (r"^page/delete_comment/(\d+)/(\d+)/$", "delete_comment"),
        (r'^([\w-]+)$', 'post'),
      
        )
urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
     url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
     #url(r'^demo/','django.views.generic.simple.direct_to_template',{'template':'demo.html'}),
     url(r'^api/', include(v1_api.urls)),
     url(r'^cm/', include(cm.urls)),
     url(r'^shop/', 'book.views.index'),
     url(r'^comments/', include('django.contrib.comments.urls')),
     url(r'^contact/', include('quix.django.contact.urls')),   
     url(r'^todo/', include(todo_resource.urls)),
     url(r'^todolist/', 'todo.views.home', name='home'),
     #url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)


