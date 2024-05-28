from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect

# Index page
def home(request):
    posts = Post.objects.all()  # Retrieve all posts
    return render(request, "blog/home.html", {'posts': posts})  # Pass the posts to the template

# Display all posts
def blog_list(request):
    posts = Post.objects.all()  # Retrieve all posts

    context = {
        'posts': posts  # Use 'posts' instead of 'blog_list'
    }
    return render(request, "blog/blog_list.html", context)

# Display details for a single post
def blog_detail(request, id):
    post = Post.objects.get(id=id)  # Retrieve the post with the given id

    context = {
        'post': post  # Use 'post' instead of 'blog_details'
    }
    return render(request, "blog/blog_detail.html", context)

def blog_delete(request, id):
    each_post = Post.objects.get(id = id)
    each_post.delete()
    return HttpResponseRedirect('/posts/')