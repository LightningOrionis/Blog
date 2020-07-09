from django.db import models
from django.utils.timezone import now as dt_now


class Blogger(models.Model):
    username = models.CharField(max_length=12)
    subscribers = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.username

    def get_subscribers_count(self):
        return self.subscribers.all().count()
    get_subscribers_count.short_description = "Subscribers"


class Comment(models.Model):
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    text = models.TextField()

    def __str__(self):
        return "{0}'s comment".format(self.author)

    class Meta:
        ordering = ["-rating", ]


class Post(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    publish_datetime = models.DateTimeField(default=dt_now())
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["rating", "-publish_datetime"]
