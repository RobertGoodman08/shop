from django import forms
from comment.models import Comment
from django.forms import ModelForm


# username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'name': 'name', 'placeholder': 'Your Full name'}), required=True)
#     comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'message', 'id': 'message', 'rows': '1', 'placeholder': 'Message'}), required=True)



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'comment', 'rate']

