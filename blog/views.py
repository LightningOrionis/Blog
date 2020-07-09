from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


class PostsListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/posts_list.html'


class BloggersListView(generic.ListView):
    model = Blogger
    context_object_name = 'bloggers'
    template_name = 'blog/bloggers_list.html'


class PostDetailView(generic.DetailView):
    pass


class BloggerDetailView(generic.DetailView):
    pass


class NewCommentForm(generic.ListView):
    pass
