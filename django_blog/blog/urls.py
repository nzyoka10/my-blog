from django.urls import path
from .views import blog_list, blog_detail, home, blog_delete  # Import the home view

urlpatterns = [
    path('', home),  # URL pattern for the home page
    path('posts/', blog_list),  # URL pattern for the blog list page
    path('posts/<int:id>/', blog_detail),  # URL pattern for the blog detail page
    path('<id>/delete/', blog_delete)
]
