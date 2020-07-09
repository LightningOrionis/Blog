from django.urls import path, include
from blog import views
from django.conf import urls

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'blog/', views.index, name='index'),
    path(r'blog/posts/', views.PostsListView.as_view(), name='posts_list'),
    path(r'blog/bloggers/', views.BloggersListView.as_view(), name='bloggers_list'),
    path(r'blog/post/(?P<pk>\d+)/', views.PostDetailView.as_view(), name='posts_detail'),
    path(r'blog/blogger/(?P<pk>\d+)/', views.BloggerDetailView.as_view(), name='blogger_detail'),
    path(r'blog/post/(?P<pk>\d+)/new_comment', views.NewCommentForm.as_view(), name='new_comment'),
]