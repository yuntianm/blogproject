from django.contrib.syndication.views import Feed
from .models import Post


class AllPostsRssFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = "Django |博客教程演示项目"
    link = "/"
    description = "Django 博客教程演示项目文章"

    def item(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] % s' % (item.category, item.title)

    def item_description(self, item):
        return item.body
