from django.contrib.sitemaps import Sitemap
from blog.models import Post

class BlogSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Post.objects.all()

  
