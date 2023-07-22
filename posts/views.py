from django.shortcuts import render
from .models import Post, Category, Author


# Create your views here.
def homepage(request):
    categories = Category.objects.all()[0:3]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': featured,
        'latest': latest,
        'categories': categories,
    }
    return render(request, 'homepage.html', context)


def post(request, slug):
    blog_post = Post.objects.get(slug=slug)
    context = {
        'blog_post': blog_post,
    }
    return render(request, 'post.html', context)


def about(request):
    return render(request, 'about_page.html')


def category_post_list(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(categories__in=[category])
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)


def all_posts(request):
    blog_post = Post.objects.order_by('-timestamp')
    context = {
        'blog_post': blog_post
    }
    return render(request, 'all_posts.html', context)
