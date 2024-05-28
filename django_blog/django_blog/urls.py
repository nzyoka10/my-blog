from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),  # Include the URLs for the home page
    path('admin/', admin.site.urls),
    path('posts/', include('blog.urls')),  # Include the URLs for the blog app
]
