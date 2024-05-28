from django.shortcuts import render
from .models import Post

# Create your views here.
def blog_list(request):
    post = Post.objects.all()

    context = {
        'blog_list':post
    }
    return render(request, "blog/blog_list.html", context)

# detailes for each single post
def blog_detail(request, id):
    each_post = Post.objects.get(id = id)

    context = {
        'blog_details':each_post
    }
    return render(request, "blog/blog_detail.html", context)

