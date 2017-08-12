from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
url(r'^$',views.index,name='index'),
url('^(?P<blog_id>[0-9]+)/$', views.blogPost, name="blogPost")
]
