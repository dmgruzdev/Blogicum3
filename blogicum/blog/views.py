from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.utils import timezone
from blog.models import Post, Category


def index(request):
    template_name = 'blog/index.html'
    posts = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-id')[:5]
    context = {'post_list': posts}
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'blog/detail.html'
    filter_condition = {
        'is_published': True,
        'category__is_published': True,
        'pub_date__lte': timezone.now(),
        'pk': post_id
    }
    post = get_object_or_404(Post, **filter_condition)
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True)
    if not category.is_published:
        raise Http404("Категория не найдена")
    category_posts = Post.objects.select_related(
        'author',
        'location',
        'category'
    ).filter(
        is_published=True,
        category=category,
        pub_date__lte=timezone.now()
    )
    context = {
        'category': category,
        'post_list': category_posts
    }
    return render(request, template_name, context)


'''def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True)
    category_posts = Post.objects.select_related(
        'author',
        'location',
        'category').filter(
            is_published=True,
            category=category,
            pub_date__lte=timezone.now()
        )
    context = {'category': category,
               'post_list': category_posts}
    return render(request, template_name, context)'''
