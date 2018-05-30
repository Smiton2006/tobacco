from django.forms import  ModelForm
from models import Comments,Article

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['article_title','article_text']        