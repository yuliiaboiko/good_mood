from django.contrib import admin
from django.urls import path

import blog.urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', (blog_urls.urlpatterns, 'blog_urls', 'blog')),
]