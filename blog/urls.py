from django.urls import path, include
from blog import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.index, name='index'),
    path('blog/posts/', views.PostsListView.as_view(), name='posts_list'),
    path('blog/bloggers/', views.BloggersListView.as_view(), name='bloggers_list'),
    path('blog/post/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('blog/blogger/<int:pk>/', views.blogger_detail_view, name='blogger_detail'),
    path('blog/post/<int:pk>/new_comment/', views.NewCommentForm.as_view(), name='new_comment'),
]