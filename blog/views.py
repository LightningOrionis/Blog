from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *
from .forms import *


def index(request):
    return render(request, 'blog/index.html')


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if not request.user.is_authenticated:
            raise PermissionDenied({"message": "You don't have permission to access",})
        if comment_form.is_valid():
            author = Blogger.objects.get(author=request.user)
            Comment.objects.create(text=comment_form.cleaned_data['text'], post=post, author=author,
                                   publish_datetime=datetime.now())
    else:
        comment_form = CommentForm()
    comments = Comment.objects.filter(post=post).order_by('-publish_datetime')
    context = {'post': post, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'blog/post_detail.html', context=context)


def blogger_detail_view(request, pk):
    blogger = get_object_or_404(Blogger, pk=pk)
    posts = Post.objects.filter(author=blogger)
    return render(request, 'blog/blogger_detail.html', context={'blogger': blogger, 'posts': posts})


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


class NewCommentForm(generic.ListView):
    pass
