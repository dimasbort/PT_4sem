from .models import *
from asgiref.sync import sync_to_async


@sync_to_async()
def get_earlier_posts(criteria):
    return Post.objects.order_by(criteria)


@sync_to_async()
def get_categories():
    return Category.objects.all()


@sync_to_async()
def get_filter_posts_by_category(category):
    return Post.objects.filter(categories__slug=category)


@sync_to_async()
def get_category_title(slug):
    return Category.objects.get(slug=slug).title

