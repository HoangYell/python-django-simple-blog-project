from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        fields = ('user', 'name', 'description')
        model = Post
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'cols': 10, 'rows': 3, 'class': 'form-control'}),
        }
