from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


class PostsListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/posts_list.html'
    ordering = ['-publish_datetime']
    paginate_by = 5


class BloggersListView(generic.ListView):
    model = Blogger
    context_object_name = 'bloggers'
    template_name = 'blog/bloggers_list.html'
    paginate_by = 5


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', context={'post': post})


def blogger_detail_view(request, pk):
    blogger = get_object_or_404(Blogger, pk=pk)
    posts = Post.objects.filter(author=blogger)
    return render(request, 'blog/blogger_detail.html', context={'blogger': blogger, 'posts': posts})


class NewCommentForm(generic.ListView):
    pass
