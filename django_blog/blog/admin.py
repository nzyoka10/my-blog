from django.contrib import admin

#  import of the models called 'Post' 
from .models import Post

# Register your models here.
admin.site.register(Post)
