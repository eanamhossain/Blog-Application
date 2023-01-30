from django import forms 
from blog.models import Post



class PostFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ('author',)


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ('categories', )
