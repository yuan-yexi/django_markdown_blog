from django.contrib import admin
from django.urls import path
from posts.views import homepage, post, about, all_posts, category_post_list

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('post/<slug>/', post, name='post'),
    path('about/', about, name='about'),
    path('postlist/<slug>/', category_post_list, name='category_post_list'),
    path('posts/', all_posts, name='all_posts')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
