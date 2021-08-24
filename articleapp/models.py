from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    # on_delete = models.CASCADE: 종속, 유저가 삭제되면 article도 삭제된다
    # on_delete = models.SET_NULL: 유저가 삭제되도 게시글은 남아있으며 작성자명은 null로 된다.

    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                               related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)

    like = models.IntegerField(default=0)