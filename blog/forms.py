from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class InputForm(forms.Form):
    name = forms.CharField(label='名前', max_length=13)
    memo = forms.CharField(label='メモ',widget=forms.Textarea(attrs={'rows':6,'cols':40}),required=False)
    check = forms.BooleanField(label='入力確認')