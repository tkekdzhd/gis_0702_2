from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] #사용자로부터 받고자 하는 데이터