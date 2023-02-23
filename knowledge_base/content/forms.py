from django import forms
from .models import Article


class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text', 'author',)

    def save(self):
        super(NewArticleForm, self).save()
