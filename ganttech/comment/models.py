from django.db import models
from django.forms import ModelForm
from home.models import Product
from django.contrib.auth.models import User



class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, verbose_name='Name')
    comment = models.CharField(max_length=250, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'comment', 'rate']
