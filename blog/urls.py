from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('api/index/', views.AllBlogPostsView.as_view(), name='posts'),
    path('api/add-comment/', views.add_comment, name='add_comment'),
    path('api/popular-posts/', views.PopularBlogPostsView.as_view(), name='popular_posts'),
    path('api/<slug:slug>/', views.get_blog_post, name='post_details'),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html'), name='blog'),
]
