from blog.models import Category, Post

from django.shortcuts import get_object_or_404, render
from django.utils import timezone


POSTS_PER_PAGE = 5


def get_base_posts_queryset():
    return Post.objects.select_related(
        'author', 'category', 'location'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    template_name = 'blog/index.html'
    posts = get_base_posts_queryset().order_by('pub_date')[:POSTS_PER_PAGE]
    context = {'post_list': posts}
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(get_base_posts_queryset(), pk=post_id)
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True)
    category_posts = get_base_posts_queryset().filter(category=category)
    context = {
        'category': category,
        'post_list': category_posts
    }
    return render(request, template_name, context)
