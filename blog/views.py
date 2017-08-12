from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import BlogPost, PostComment
# Create your views here.
def index(request):
    latest_blog_lst = BlogPost.objects.order_by('-timestamp')[:5]
    context = {
    'posts': latest_blog_lst
    }
    return render(request, 'blog/index.html', context)

def blogPost(request, blog_id):
    # blogPost = get_object_or_404(BlogPost, pk=blog_id)
    post = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'blog/blogpost.html', {'post': post, 'comments': post.postcomment_set.all() })
