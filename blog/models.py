from django.db import models
from django.urls import reverse
from account.models import User


class Blogger(models.Model):
    subscribers = models.ManyToManyField("self", blank=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username

    def get_subscribers_count(self):
        return self.subscribers.all().count()

    def get_absolute_url(self):
        return reverse('blogger_detail', args=[str(self.pk)])

    get_subscribers_count.short_description = "Subscribers"


class Post(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    publish_datetime = models.DateTimeField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

    class Meta:
        ordering = ["-publish_datetime"]


class Comment(models.Model):
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE, blank=True)
    rating = models.IntegerField(default=0)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    publish_datetime = models.DateTimeField()

    def __str__(self):
        return "{0} comment".format(self.pk)

    class Meta:
        ordering = ['publish_datetime']
