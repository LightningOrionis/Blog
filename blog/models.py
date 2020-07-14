from django.db import models
from django.urls import reverse


class Blogger(models.Model):
    username = models.CharField(max_length=12)
    subscribers = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.username

    def get_subscribers_count(self):
        return self.subscribers.all().count()

    def get_absolute_url(self):
        return reverse('blogger_detail', args=[str(self.pk)])

    get_subscribers_count.short_description = "Subscribers"


class Comment(models.Model):
    #author = models.OneToOneField(Blogger, on_delete=models.CASCADE, blank=True)
    rating = models.IntegerField(default=0)
    text = models.TextField()

    def __str__(self):
        return "{0} comment".format(self.pk)


class Post(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    publish_datetime = models.DateTimeField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

    class Meta:
        ordering = ["-publish_datetime"]

