from django.core.exceptions import ValidationError
from .models import *
from django.forms import ModelForm
from datetime import datetime


class PostForm(ModelForm):
    def clean_publish_datetime(self):
        data = self.cleaned_data['publish_datetime']
        if data < datetime.now():
            raise ValidationError('Invalid date - publish in past')
        return data

    class Meta:
        model = Post
        fields = ['title', 'text', 'publish_datetime']
        labels = {'title': 'Title', 'text': 'Text', 'publish_datetime': 'Publish Date and Time'}


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': ''}
        help_text = 'Input your comment'

